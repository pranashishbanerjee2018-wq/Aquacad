/**
 * AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
 * File: app.js
 * 
 * Master Presentation State Machine & Timeline Orchestrator.
 * Total Presentation Duration: 165 Seconds (2 minutes 45 seconds).
 * Features 7 Continuous Scenes, Dual-Researcher Gestures,
 * Multi-Stage Animated Machine, and MATLAB Scientific Integration.
 */

class AquaCardPresentationApp {
  constructor() {
    this.TOTAL_DURATION = 165.0; // Exact 165 seconds
    this.currentTime = 0.0;
    this.isPlaying = false;
    this.isPaused = false;
    this.showSubtitles = true;
    this.currentSceneIdx = 0;
    this.currentLineIdx = -1;
    this.playbackInterval = null;

    // Subsystems
    this.speechCoord = new window.SpeechCoordinator();
    this.labEffects = new window.LabEffectsEngine();
    this.matlabViewer = new window.MatlabViewer();

    // Scene definitions (Exactly 7 scenes, strict boundaries)
    this.scenes = [
      {
        id: 1,
        title: "The Global Water Challenge",
        start: 0.0,
        end: 22.0,
        desc: "Escalating water quality pressures & static treatment limitations."
      },
      {
        id: 2,
        title: "Introducing AQUACARD",
        start: 22.0,
        end: 44.0,
        desc: "Smart purification architecture & sensor integration revealed."
      },
      {
        id: 3,
        title: "The Sensor Intelligence",
        start: 44.0,
        end: 68.0,
        desc: "Multi-parametric diagnostic telemetry & process indicators."
      },
      {
        id: 4,
        title: "AI-Powered Purification",
        start: 68.0,
        end: 93.0,
        desc: "Sequential sediment, carbon, dynamic membrane, & UV stages."
      },
      {
        id: 5,
        title: "MATLAB Scientific Monitoring",
        start: 93.0,
        end: 120.0,
        desc: "AquaCard.m classification modeling, confusion matrix, & trends."
      },
      {
        id: 6,
        title: "Intelligent Management",
        start: 120.0,
        end: 145.0,
        desc: "Predictive maintenance, pressure monitoring, & adaptive control."
      },
      {
        id: 7,
        title: "The Future of Water Technology",
        start: 145.0,
        end: 165.0,
        desc: "Explainable AI, sustainable stewardship, & closing remarks."
      }
    ];

    // Master dialogue script (334 words across 15 spoken lines)
    this.dialogueLines = [
      // SCENE 1 (0:00 - 0:22)
      {
        sceneId: 1,
        speaker: 'adrian',
        start: 0.5,
        end: 11.0,
        text: "Welcome to our laboratory. Across the globe, clean water access faces immense pressure from industrial pollution and climate volatility, while conventional treatment systems operate blindly without telemetry."
      },
      {
        sceneId: 1,
        speaker: 'ethan',
        start: 11.5,
        end: 21.5,
        text: "Traditional plants run on fixed schedules, unable to respond to sudden contaminant spikes. We asked: what if purification could actively sense, reason, and adapt?"
      },

      // SCENE 2 (0:22 - 0:44)
      {
        sceneId: 2,
        speaker: 'adrian',
        start: 22.5,
        end: 33.0,
        text: "Meet AQUACARD: an intelligent purification prototype integrating multi-sensor diagnostics, explainable machine-learning, and reconfigurable physical filtration stages into a unified architecture."
      },
      {
        sceneId: 2,
        speaker: 'ethan',
        start: 33.5,
        end: 43.5,
        text: "From raw intake to output verification, AQUACARD orchestrates physical treatment using continuous empirical telemetry rather than arbitrary timers."
      },

      // SCENE 3 (0:44 - 1:08)
      {
        sceneId: 3,
        speaker: 'ethan',
        start: 44.5,
        end: 55.5,
        text: "Influent enters our primary chamber, where probes capture pH, optical turbidity, total dissolved solids, electrical conductivity, temperature, and differential pressure."
      },
      {
        sceneId: 3,
        speaker: 'adrian',
        start: 56.0,
        end: 67.5,
        text: "Crucially, these physical sensors provide process indicators rather than full microbiological assays. The telemetry feeds our AI classifier to characterize incoming water regimes in real time."
      },

      // SCENE 4 (1:08 - 1:33)
      {
        sceneId: 4,
        speaker: 'adrian',
        start: 68.5,
        end: 79.5,
        text: "Our explainable algorithm activates optimal routes: sediment filtering for suspended matter, activated carbon for chlorine and organics, membrane separation, and ultraviolet irradiation."
      },
      {
        sceneId: 4,
        speaker: 'ethan',
        start: 80.0,
        end: 92.0,
        text: "When dissolved solids remain low, the high-pressure reverse osmosis membrane is bypassed, slashing energy demand while sediment and UV stages neutralize particulates and bacteria."
      },

      // SCENE 5 (1:33 - 2:00)
      {
        sceneId: 5,
        speaker: 'ethan',
        start: 93.5,
        end: 106.0,
        text: "We validated the system using our MATLAB simulation script, AquaCard.m. Using a multi-class k-nearest neighbors classifier, our algorithm achieved ninety-five point eight percent accuracy across four operational regimes."
      },
      {
        sceneId: 5,
        speaker: 'adrian',
        start: 106.5,
        end: 119.5,
        text: "The confusion matrix demonstrates reliable separation between normal baseline water and elevated turbidity or salinity, providing fully explainable decision boundaries for automated valve modulation."
      },

      // SCENE 6 (2:00 - 2:25)
      {
        sceneId: 6,
        speaker: 'ethan',
        start: 120.5,
        end: 132.0,
        text: "AQUACARD continuously tracks hydraulic pressure gradients across filter membranes. By detecting early cake formation and particulate buildup, it triggers predictive backwash and maintenance alerts before clogging."
      },
      {
        sceneId: 6,
        speaker: 'adrian',
        start: 132.5,
        end: 144.5,
        text: "This closed-loop flow control balances hydraulic throughput against energy consumption, extending cartridge longevity while ensuring operating parameters remain strictly within calibrated engineering safety boundaries."
      },

      // SCENE 7 (2:25 - 2:45)
      {
        sceneId: 7,
        speaker: 'adrian',
        start: 145.5,
        end: 154.5,
        text: "AQUACARD demonstrates that artificial intelligence and embedded sensor telemetry can transform water purification into a sustainable, transparent, and responsive infrastructure."
      },
      {
        sceneId: 7,
        speaker: 'ethan',
        start: 155.0,
        end: 161.0,
        text: "While certified laboratory testing remains essential for drinking potability, intelligent monitoring makes every treatment stage proactive and efficient."
      },
      {
        sceneId: 7,
        speaker: 'adrian',
        start: 161.5,
        end: 164.5,
        text: "AQUACARD — Because the future of clean water begins with intelligent decisions."
      }
    ];
  }

  init() {
    console.log('[AQUACARD APP] Initializing Master Engine...');
    this.bindDOM();
    this.matlabViewer.loadResults();
    this.labEffects.initFluidCanvas('fluid-particles-canvas');
    this.labEffects.initNaturalBlinking();
    this.renderSceneMarkers();
    this.updateTimelineUI();
    this.resizeStage();

    window.addEventListener('resize', () => this.resizeStage());
  }

  resizeStage() {
    const stage = document.getElementById('stage');
    if (!stage) return;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    const scale = Math.min(windowWidth / 1920, windowHeight / 1080);
    stage.style.transform = `scale(${scale})`;
  }

  bindDOM() {
    // Start presentation button on landing screen
    const btnStart = document.getElementById('btn-start-presentation');
    if (btnStart) {
      btnStart.addEventListener('click', () => {
        const landing = document.getElementById('landing-screen');
        if (landing) landing.style.display = 'none';
        this.labEffects.initAudio();
        this.play();
      });
    }

    // Play/Pause button
    const btnPlayPause = document.getElementById('btn-play-pause');
    if (btnPlayPause) {
      btnPlayPause.addEventListener('click', () => {
        if (this.isPlaying) {
          this.pause();
        } else {
          this.play();
        }
      });
    }

    // Restart button
    const btnRestart = document.getElementById('btn-restart');
    if (btnRestart) {
      btnRestart.addEventListener('click', () => this.restart());
    }

    // Next / Previous Scene buttons
    const btnPrev = document.getElementById('btn-prev-scene');
    if (btnPrev) {
      btnPrev.addEventListener('click', () => this.jumpToPrevScene());
    }
    const btnNext = document.getElementById('btn-next-scene');
    if (btnNext) {
      btnNext.addEventListener('click', () => this.jumpToNextScene());
    }

    // Subtitles toggle
    const btnSub = document.getElementById('btn-toggle-subtitles');
    if (btnSub) {
      btnSub.addEventListener('click', () => {
        this.showSubtitles = !this.showSubtitles;
        const subBox = document.getElementById('subtitle-container');
        if (subBox) subBox.style.display = this.showSubtitles ? 'flex' : 'none';
        btnSub.classList.toggle('active', this.showSubtitles);
      });
    }

    // Sound toggle
    const btnSound = document.getElementById('btn-toggle-sound');
    if (btnSound) {
      btnSound.addEventListener('click', () => {
        const muted = !this.labEffects.isMuted;
        this.labEffects.setMuted(muted);
        this.speechCoord.setMuted(muted);
        btnSound.classList.toggle('active', !muted);
      });
    }

    // Fullscreen toggle
    const btnFull = document.getElementById('btn-toggle-fullscreen');
    if (btnFull) {
      btnFull.addEventListener('click', () => this.toggleFullscreen());
    }

    // Timeline scrubber click
    const track = document.getElementById('progress-track');
    if (track) {
      track.addEventListener('click', (e) => {
        const rect = track.getBoundingClientRect();
        const clickRatio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
        this.seek(clickRatio * this.TOTAL_DURATION);
      });
    }

    // MATLAB Viewer Tabs in Scene 5 / modal
    document.querySelectorAll('.matlab-tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const plot = e.target.dataset.plot;
        this.matlabViewer.selectPlot(plot);
      });
    });

    // Replay presentation button on final screen
    const btnReplay = document.getElementById('btn-replay-presentation');
    if (btnReplay) {
      btnReplay.addEventListener('click', () => {
        const finalScreen = document.getElementById('final-screen');
        if (finalScreen) finalScreen.classList.remove('visible');
        this.restart();
      });
    }
  }

  renderSceneMarkers() {
    const markersContainer = document.getElementById('scene-markers');
    if (!markersContainer) return;
    markersContainer.innerHTML = '';

    this.scenes.forEach(scene => {
      const marker = document.createElement('div');
      marker.className = 'scene-marker';
      marker.style.left = `${(scene.start / this.TOTAL_DURATION) * 100}%`;
      marker.title = `Scene ${scene.id}: ${scene.title}`;
      markersContainer.appendChild(marker);
    });
  }

  play() {
    this.isPlaying = true;
    this.isPaused = false;
    this.speechCoord.resume();
    this.updatePlayPauseBtn(true);

    if (this.playbackInterval) clearInterval(this.playbackInterval);

    const stepMs = 100;
    this.playbackInterval = setInterval(() => {
      this.currentTime += stepMs / 1000;

      if (this.currentTime >= this.TOTAL_DURATION) {
        this.currentTime = this.TOTAL_DURATION;
        this.completePresentation();
        return;
      }

      this.tick();
    }, stepMs);
  }

  pause() {
    this.isPlaying = false;
    this.isPaused = true;
    if (this.playbackInterval) {
      clearInterval(this.playbackInterval);
      this.playbackInterval = null;
    }
    this.speechCoord.pause();
    this.updatePlayPauseBtn(false);
  }

  restart() {
    this.pause();
    this.currentTime = 0.0;
    this.currentLineIdx = -1;
    this.currentSceneIdx = 0;
    this.speechCoord.stop();
    this.speechCoord.resetMouths();

    // Reset machine state
    const machine = document.getElementById('aquacard-machine-layer');
    if (machine) machine.style.transform = 'scale(1) translateY(0)';

    const finalScreen = document.getElementById('final-screen');
    if (finalScreen) finalScreen.classList.remove('visible');

    this.updateTimelineUI();
    this.play();
  }

  seek(targetTime) {
    const wasPlaying = this.isPlaying;
    if (wasPlaying) this.pause();

    this.currentTime = Math.max(0, Math.min(this.TOTAL_DURATION, targetTime));
    this.currentLineIdx = -1;
    this.speechCoord.stop();
    this.speechCoord.resetMouths();
    this.tick();

    if (wasPlaying) this.play();
  }

  jumpToPrevScene() {
    const curIdx = this.getSceneIndexAtTime(this.currentTime);
    if (curIdx > 0) {
      this.seek(this.scenes[curIdx - 1].start);
    } else {
      this.seek(0);
    }
  }

  jumpToNextScene() {
    const curIdx = this.getSceneIndexAtTime(this.currentTime);
    if (curIdx < this.scenes.length - 1) {
      this.seek(this.scenes[curIdx + 1].start);
    }
  }

  getSceneIndexAtTime(t) {
    for (let i = 0; i < this.scenes.length; i++) {
      if (t >= this.scenes[i].start && t < this.scenes[i].end) {
        return i;
      }
    }
    return this.scenes.length - 1;
  }

  tick() {
    this.updateTimelineUI();

    // Update active scene
    const sceneIdx = this.getSceneIndexAtTime(this.currentTime);
    if (sceneIdx !== this.currentSceneIdx) {
      this.currentSceneIdx = sceneIdx;
      this.onSceneTransition(this.scenes[sceneIdx]);
    }

    // Check dialogue triggers
    this.checkDialogue();
  }

  checkDialogue() {
    // Find matching line for current timestamp
    const activeLineIdx = this.dialogueLines.findIndex(
      line => this.currentTime >= line.start && this.currentTime < line.end
    );

    if (activeLineIdx !== -1 && activeLineIdx !== this.currentLineIdx) {
      this.currentLineIdx = activeLineIdx;
      const line = this.dialogueLines[activeLineIdx];
      this.triggerSpokenLine(line);
    } else if (activeLineIdx === -1 && this.currentLineIdx !== -1) {
      // In silence gap between lines
      this.currentLineIdx = -1;
      this.speechCoord.resetMouths();
      this.clearSubtitleHighlight();
    }
  }

  triggerSpokenLine(line) {
    const duration = line.end - line.start;

    // Subtitle update
    this.updateSubtitles(line.speaker, line.text);

    // Speaker highlighting and gestures
    this.setSpeakerActive(line.speaker);

    // Speak audio & lip-sync
    this.speechCoord.speakLine(line.speaker, line.text, duration, () => {
      this.speechCoord.resetMouths();
    });
  }

  onSceneTransition(scene) {
    console.log(`[AQUACARD] Transitioning to Scene ${scene.id}: ${scene.title}`);

    // Update scene badge
    const badgeNum = document.querySelector('#scene-badge .scene-number');
    const badgeTitle = document.querySelector('#scene-badge .scene-title');
    if (badgeNum) badgeNum.textContent = `SCENE ${scene.id} / 7`;
    if (badgeTitle) badgeTitle.textContent = scene.title;

    // Hide all hud widgets first
    document.querySelectorAll('.hud-widget').forEach(w => w.classList.remove('visible'));

    const adrianChar = document.getElementById('character-adrian');
    const ethanChar = document.getElementById('character-ethan');
    const machine = document.getElementById('aquacard-machine-layer');

    // Scene-specific choreography & HUD activation
    switch (scene.id) {
      case 1:
        // Scene 1: The Global Water Challenge
        if (adrianChar) adrianChar.style.transform = 'scale(1) translateX(0)';
        if (ethanChar) ethanChar.style.transform = 'scale(1) translateX(0)';
        if (machine) machine.style.transform = 'scale(1) translateY(0)';
        break;

      case 2:
        // Scene 2: Introducing AQUACARD
        if (machine) {
          machine.style.transform = 'scale(1.04) translateY(-10px)';
          machine.style.filter = 'drop-shadow(0 0 20px rgba(0, 229, 255, 0.4))';
        }
        break;

      case 3:
        // Scene 3: The Sensor Intelligence
        const sensorMatrix = document.getElementById('widget-sensor-matrix');
        if (sensorMatrix) sensorMatrix.classList.add('visible');
        this.labEffects.playTelemetryChirp();
        break;

      case 4:
        // Scene 4: AI-Powered Purification
        const purifFlow = document.getElementById('widget-purification-flow');
        if (purifFlow) purifFlow.classList.add('visible');
        if (machine) machine.style.transform = 'scale(1.05) translateY(-15px)';
        break;

      case 5:
        // Scene 5: MATLAB Scientific Monitoring
        const matlabPanel = document.getElementById('widget-matlab-panel');
        if (matlabPanel) {
          matlabPanel.classList.add('visible');
          this.matlabViewer.selectPlot('confusion_matrix');
        }
        break;

      case 6:
        // Scene 6: Intelligent Management (Predictive alert)
        const alertWidget = document.getElementById('widget-predictive-alert');
        if (alertWidget) alertWidget.classList.add('visible');
        this.labEffects.playWarningChime();
        break;

      case 7:
        // Scene 7: The Future of Water Technology
        if (adrianChar) adrianChar.style.transform = 'scale(1.03) translateX(30px)';
        if (ethanChar) ethanChar.style.transform = 'scale(1.03) translateX(-30px)';
        if (machine) {
          machine.style.transform = 'scale(1.06) translateY(-20px)';
          machine.style.filter = 'drop-shadow(0 0 30px rgba(0, 229, 255, 0.6))';
        }
        break;
    }
  }

  setSpeakerActive(speaker) {
    const adrianChar = document.getElementById('character-adrian');
    const ethanChar = document.getElementById('character-ethan');

    if (speaker === 'adrian') {
      if (adrianChar) {
        adrianChar.classList.add('speaker-active');
        adrianChar.classList.add('anim-speaking-head');
        adrianChar.classList.remove('anim-listening-nod');
      }
      if (ethanChar) {
        ethanChar.classList.remove('speaker-active');
        ethanChar.classList.remove('anim-speaking-head');
        ethanChar.classList.add('anim-listening-nod'); // collegiate nod
      }
    } else {
      if (ethanChar) {
        ethanChar.classList.add('speaker-active');
        ethanChar.classList.add('anim-speaking-head');
        ethanChar.classList.remove('anim-listening-nod');
      }
      if (adrianChar) {
        adrianChar.classList.remove('speaker-active');
        adrianChar.classList.remove('anim-speaking-head');
        adrianChar.classList.add('anim-listening-nod'); // collegiate nod
      }
    }
  }

  clearSubtitleHighlight() {
    const adrianChar = document.getElementById('character-adrian');
    const ethanChar = document.getElementById('character-ethan');
    if (adrianChar) {
      adrianChar.classList.remove('speaker-active', 'anim-speaking-head');
    }
    if (ethanChar) {
      ethanChar.classList.remove('speaker-active', 'anim-speaking-head');
    }
  }

  updateSubtitles(speaker, text) {
    const tagEl = document.getElementById('speaker-tag');
    const textEl = document.getElementById('subtitle-text');
    if (!tagEl || !textEl) return;

    if (speaker === 'adrian') {
      tagEl.className = 'speaker-tag adrian';
      tagEl.textContent = 'DR. ADRIAN REYNOLDS';
    } else {
      tagEl.className = 'speaker-tag ethan';
      tagEl.textContent = 'ETHAN CARTER';
    }
    textEl.textContent = text;
  }

  updateTimelineUI() {
    // Time text
    const curTimeEl = document.getElementById('time-current');
    const totalTimeEl = document.getElementById('time-total');
    if (curTimeEl) curTimeEl.textContent = this.formatTime(this.currentTime);
    if (totalTimeEl) totalTimeEl.textContent = this.formatTime(this.TOTAL_DURATION);

    // Progress bar fill
    const fill = document.getElementById('progress-fill');
    if (fill) {
      const pct = (this.currentTime / this.TOTAL_DURATION) * 100;
      fill.style.width = `${pct}%`;
    }
  }

  updatePlayPauseBtn(playing) {
    const btn = document.getElementById('btn-play-pause');
    if (!btn) return;
    if (playing) {
      btn.innerHTML = `
        <svg viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
      `;
      btn.title = 'Pause';
    } else {
      btn.innerHTML = `
        <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      `;
      btn.title = 'Play';
    }
  }

  formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  }

  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) document.exitFullscreen();
    }
  }

  completePresentation() {
    this.pause();
    this.speechCoord.resetMouths();
    const finalScreen = document.getElementById('final-screen');
    if (finalScreen) finalScreen.classList.add('visible');
    console.log('[AQUACARD] Presentation reached full 165s conclusion.');
  }
}

// Auto instantiate on DOM load
window.addEventListener('DOMContentLoaded', () => {
  window.aquaApp = new AquaCardPresentationApp();
  window.aquaApp.init();
});
