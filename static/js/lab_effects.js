/**
 * AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
 * File: lab_effects.js
 * 
 * Procedural Audio Synthesizer, Dynamic Fluid Particles Engine,
 * and Realistic Character Eye-Blink Dynamics.
 */

class LabEffectsEngine {
  constructor() {
    this.audioCtx = null;
    this.ambientGain = null;
    this.waterGain = null;
    this.isMuted = false;
    this.particles = [];
    this.canvas = null;
    this.ctx = null;
    this.animFrameId = null;
    this.blinkTimers = { adrian: null, ethan: null };
  }

  initAudio() {
    if (this.audioCtx) return;
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.audioCtx = new AudioContext();

      // Master ambient gain
      this.ambientGain = this.audioCtx.createGain();
      this.ambientGain.gain.setValueAtTime(0.12, this.audioCtx.currentTime);
      this.ambientGain.connect(this.audioCtx.destination);

      // Water rush gain
      this.waterGain = this.audioCtx.createGain();
      this.waterGain.gain.setValueAtTime(0.08, this.audioCtx.currentTime);
      this.waterGain.connect(this.audioCtx.destination);

      this.startAmbientHum();
      this.startWaterLoop();
    } catch (e) {
      console.warn('Web Audio not supported or blocked:', e);
    }
  }

  startAmbientHum() {
    if (!this.audioCtx) return;
    // Dual low frequency oscillators (55Hz & 110Hz) to simulate cleanroom transformer hum
    const osc1 = this.audioCtx.createOscillator();
    const osc2 = this.audioCtx.createOscillator();
    osc1.type = 'sine';
    osc1.frequency.setValueAtTime(55, this.audioCtx.currentTime);
    osc2.type = 'triangle';
    osc2.frequency.setValueAtTime(110, this.audioCtx.currentTime);

    const filter = this.audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(180, this.audioCtx.currentTime);

    osc1.connect(filter);
    osc2.connect(filter);
    filter.connect(this.ambientGain);

    osc1.start();
    osc2.start();
  }

  startWaterLoop() {
    if (!this.audioCtx) return;
    // Filtered pink/white noise buffer for laminar fluid rush
    const bufferSize = this.audioCtx.sampleRate * 2;
    const noiseBuffer = this.audioCtx.createBuffer(1, bufferSize, this.audioCtx.sampleRate);
    const output = noiseBuffer.getChannelData(0);
    let b0 = 0, b1 = 0, b2 = 0;
    for (let i = 0; i < bufferSize; i++) {
      const white = Math.random() * 2 - 1;
      b0 = 0.99886 * b0 + white * 0.0555179;
      b1 = 0.99332 * b1 + white * 0.0750759;
      b2 = 0.96900 * b2 + white * 0.1538520;
      output[i] = (b0 + b1 + b2) * 0.08;
    }

    const whiteNoise = this.audioCtx.createBufferSource();
    whiteNoise.buffer = noiseBuffer;
    whiteNoise.loop = true;

    const filter = this.audioCtx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(450, this.audioCtx.currentTime);
    filter.Q.setValueAtTime(1.8, this.audioCtx.currentTime);

    whiteNoise.connect(filter);
    filter.connect(this.waterGain);
    whiteNoise.start();
  }

  playTelemetryChirp() {
    if (this.isMuted || !this.audioCtx) return;
    try {
      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();
      osc.type = 'sine';
      const now = this.audioCtx.currentTime;
      osc.frequency.setValueAtTime(880, now);
      osc.frequency.exponentialRampToValueAtTime(1320, now + 0.15);
      gain.gain.setValueAtTime(0.06, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.16);
    } catch (e) {}
  }

  playWarningChime() {
    if (this.isMuted || !this.audioCtx) return;
    try {
      const now = this.audioCtx.currentTime;
      [440, 554, 659].forEach((f, idx) => {
        const osc = this.audioCtx.createOscillator();
        const gain = this.audioCtx.createGain();
        osc.frequency.setValueAtTime(f, now + idx * 0.08);
        gain.gain.setValueAtTime(0.08, now + idx * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.25);
        osc.connect(gain);
        gain.connect(this.audioCtx.destination);
        osc.start(now + idx * 0.08);
        osc.stop(now + idx * 0.08 + 0.26);
      });
    } catch (e) {}
  }

  setMuted(muted) {
    this.isMuted = muted;
    if (this.ambientGain && this.waterGain && this.audioCtx) {
      const val = muted ? 0.0 : 0.12;
      this.ambientGain.gain.setValueAtTime(val, this.audioCtx.currentTime);
      this.waterGain.gain.setValueAtTime(muted ? 0.0 : 0.08, this.audioCtx.currentTime);
    }
  }

  // =========================================================================
  // DYNAMIC FLUID PARTICLE CANVAS ENGINE
  // =========================================================================
  initFluidCanvas(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.canvas.width = 1920;
    this.canvas.height = 1080;

    // Initialize 160 fluid particles across the machine chambers
    this.particles = [];
    // Machine is positioned at left: 510px, bottom: 80px (Y: 350 to 950 approx)
    // Chamber centers X roughly:
    // Ch1: 675, Ch2: 825, Ch3: 975, Ch4: 1125, Ch5: 1275
    for (let i = 0; i < 150; i++) {
      this.particles.push(this.createParticle(true));
    }

    this.renderParticles = this.renderParticles.bind(this);
    this.renderParticles();
  }

  createParticle(randomStart = false) {
    // Flow starts at Chamber 1 (X: ~640-720) and progresses rightward to Chamber 5 (~1240-1320)
    const stage = randomStart ? Math.floor(Math.random() * 5) : 0;
    const stageX = [680, 830, 980, 1130, 1280];
    const xBase = stageX[stage];

    let color = '#a3824c'; // Turbid brown/amber for stage 0
    if (stage === 1) color = '#5ca0ba'; // Filtered teal
    if (stage === 2) color = '#38bdf8'; // Clean cyan
    if (stage === 3) color = '#00e5ff'; // Pure aqua
    if (stage >= 4) color = '#c084fc'; // UV irradiated pure

    return {
      x: xBase + (Math.random() * 60 - 30),
      y: randomStart ? (500 + Math.random() * 260) : (500 + Math.random() * 40),
      vx: (Math.random() - 0.5) * 0.4,
      vy: 0.8 + Math.random() * 1.4,
      size: 1.5 + Math.random() * 2.5,
      stage: stage,
      color: color,
      alpha: 0.5 + Math.random() * 0.5,
      life: 0
    };
  }

  renderParticles() {
    if (!this.ctx || !this.canvas) return;
    this.ctx.clearRect(0, 0, 1920, 1080);

    const stageX = [680, 830, 980, 1130, 1280];

    for (let i = 0; i < this.particles.length; i++) {
      const p = this.particles[i];
      p.y += p.vy;
      p.x += p.vx;
      p.life++;

      // When reaching bottom of chamber, advance to next stage or reset
      if (p.y > 810) {
        if (p.stage < 4) {
          p.stage++;
          p.x = stageX[p.stage] + (Math.random() * 60 - 30);
          p.y = 510;
          if (p.stage === 1) p.color = '#5ca0ba';
          if (p.stage === 2) p.color = '#38bdf8';
          if (p.stage === 3) p.color = '#00e5ff';
          if (p.stage === 4) p.color = '#c084fc';
        } else {
          // Reached end of UV chamber; recycle to raw intake
          Object.assign(p, this.createParticle(false));
        }
      }

      // Draw particle bubble
      this.ctx.save();
      this.ctx.globalAlpha = p.alpha;
      this.ctx.fillStyle = p.color;
      this.ctx.beginPath();
      this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
      this.ctx.fill();
      this.ctx.restore();
    }

    this.animFrameId = requestAnimationFrame(this.renderParticles);
  }

  // =========================================================================
  // NATURAL CHARACTER BLINKING
  // =========================================================================
  initNaturalBlinking() {
    // Dr. Adrian Reynolds Blink cycle (every 3.8 to 5.2s)
    const scheduleAdrianBlink = () => {
      const delay = 3500 + Math.random() * 2000;
      this.blinkTimers.adrian = setTimeout(() => {
        const blinkEl = document.getElementById('adrian-blink');
        if (blinkEl) {
          blinkEl.style.opacity = '1';
          setTimeout(() => {
            blinkEl.style.opacity = '0';
            scheduleAdrianBlink();
          }, 140);
        } else {
          scheduleAdrianBlink();
        }
      }, delay);
    };

    // Ethan Carter Blink cycle (every 3.2 to 4.8s)
    const scheduleEthanBlink = () => {
      const delay = 3000 + Math.random() * 2200;
      this.blinkTimers.ethan = setTimeout(() => {
        const blinkEl = document.getElementById('ethan-blink');
        if (blinkEl) {
          blinkEl.style.opacity = '1';
          setTimeout(() => {
            blinkEl.style.opacity = '0';
            scheduleEthanBlink();
          }, 130);
        } else {
          scheduleEthanBlink();
        }
      }, delay);
    };

    scheduleAdrianBlink();
    scheduleEthanBlink();
  }

  destroy() {
    if (this.animFrameId) cancelAnimationFrame(this.animFrameId);
    if (this.blinkTimers.adrian) clearTimeout(this.blinkTimers.adrian);
    if (this.blinkTimers.ethan) clearTimeout(this.blinkTimers.ethan);
    if (this.audioCtx) this.audioCtx.close();
  }
}

window.LabEffectsEngine = LabEffectsEngine;
