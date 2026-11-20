/**
 * AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
 * File: speech.js
 * 
 * Lip-synchronization & speech synthesis coordinator.
 * Supports Web Speech API (speechSynthesis) and Web Audio API tone synthesis.
 * Features 5 distinct phoneme-viseme mouth shapes for both researchers.
 */

class SpeechCoordinator {
  constructor() {
    this.synth = window.speechSynthesis || null;
    this.voices = [];
    this.isMuted = false;
    this.isSpeaking = false;
    this.currentUtterance = null;
    this.visemeTimer = null;
    this.activeSpeaker = null;

    // Load available voices
    if (this.synth) {
      this.synth.onvoiceschanged = () => {
        this.voices = this.synth.getVoices();
      };
      this.voices = this.synth.getVoices();
    }

    // Viseme IDs mapped to each character SVG
    this.visemeMap = {
      adrian: {
        rest: 'adrian-mouth-rest',
        vowel_a: 'adrian-mouth-vowel-a',
        round_o: 'adrian-mouth-round-o',
        wide_e: 'adrian-mouth-wide-e',
        mid: 'adrian-mouth-mid'
      },
      ethan: {
        rest: 'ethan-mouth-rest',
        vowel_a: 'ethan-mouth-vowel-a',
        round_o: 'ethan-mouth-round-o',
        wide_e: 'ethan-mouth-wide-e',
        mid: 'ethan-mouth-mid'
      }
    };
  }

  setMuted(muted) {
    this.isMuted = muted;
    if (this.isMuted && this.synth) {
      this.synth.cancel();
    }
  }

  /**
   * Sets mouth viseme shape for given character.
   */
  setViseme(speaker, visemeKey) {
    const charMap = this.visemeMap[speaker];
    if (!charMap) return;

    Object.keys(charMap).forEach(key => {
      const el = document.getElementById(charMap[key]);
      if (el) {
        if (key === visemeKey) {
          el.style.display = 'inline';
        } else {
          el.style.display = 'none';
        }
      }
    });
  }

  /**
   * Resets both characters' mouths to the closed resting shape.
   */
  resetMouths() {
    if (this.visemeTimer) {
      clearInterval(this.visemeTimer);
      this.visemeTimer = null;
    }
    this.setViseme('adrian', 'rest');
    this.setViseme('ethan', 'rest');
    this.activeSpeaker = null;
    this.isSpeaking = false;
  }

  /**
   * Starts procedural lip-sync animation cycling through realistic visemes
   * corresponding to phonetic rhythms of spoken speech.
   */
  startLipSync(speaker, durationSec) {
    this.resetMouths();
    this.activeSpeaker = speaker;
    this.isSpeaking = true;

    // Ensure the other character has mouth closed
    const otherSpeaker = (speaker === 'adrian') ? 'ethan' : 'adrian';
    this.setViseme(otherSpeaker, 'rest');

    const visemes = ['vowel_a', 'mid', 'wide_e', 'round_o', 'mid', 'vowel_a', 'rest'];
    let idx = 0;

    // Change visemes every 110-180ms to mimic natural syllables
    this.visemeTimer = setInterval(() => {
      if (!this.isSpeaking) return;
      const viseme = visemes[idx % visemes.length];
      this.setViseme(speaker, viseme);
      idx++;
    }, 135);

    // Auto close mouth when line duration elapses
    setTimeout(() => {
      if (this.activeSpeaker === speaker) {
        this.resetMouths();
      }
    }, durationSec * 1000);
  }

  /**
   * Speaks a dialogue line with synchronized lip-sync.
   */
  speakLine(speaker, text, durationSec, onEndCallback) {
    this.resetMouths();

    // Trigger visual lip sync
    this.startLipSync(speaker, durationSec);

    if (this.isMuted || !this.synth) {
      // Audio is muted or Web Speech unsupported; run timer and callback
      setTimeout(() => {
        this.resetMouths();
        if (onEndCallback) onEndCallback();
      }, durationSec * 1000);
      return;
    }

    try {
      this.synth.cancel(); // Stop any pending speech
      const utter = new SpeechSynthesisUtterance(text);
      this.currentUtterance = utter;

      // Select distinct acoustic parameters per inventor
      if (speaker === 'adrian') {
        // Dr. Adrian Reynolds: Senior, deep, analytical
        utter.rate = 0.94;
        utter.pitch = 0.85;
        const maleVoice = this.voices.find(v => (v.name.includes('David') || v.name.includes('Male') || v.name.includes('Natural')) && v.lang.startsWith('en'));
        if (maleVoice) utter.voice = maleVoice;
      } else {
        // Ethan Carter: Junior, enthusiastic, energetic
        utter.rate = 1.04;
        utter.pitch = 1.15;
        const youngVoice = this.voices.find(v => (v.name.includes('Mark') || v.name.includes('George') || v.name.includes('Guy') || v.name.includes('English')) && v.lang.startsWith('en'));
        if (youngVoice) utter.voice = youngVoice;
      }

      utter.onend = () => {
        this.resetMouths();
        if (onEndCallback) onEndCallback();
      };

      utter.onerror = (e) => {
        console.warn('SpeechSynthesis error:', e);
        this.resetMouths();
        if (onEndCallback) onEndCallback();
      };

      this.synth.speak(utter);
    } catch (err) {
      console.warn('Speech error fallback:', err);
      setTimeout(() => {
        this.resetMouths();
        if (onEndCallback) onEndCallback();
      }, durationSec * 1000);
    }
  }

  pause() {
    this.isSpeaking = false;
    if (this.visemeTimer) {
      clearInterval(this.visemeTimer);
      this.visemeTimer = null;
    }
    if (this.synth && this.synth.speaking) {
      this.synth.pause();
    }
  }

  resume() {
    if (this.activeSpeaker) {
      this.isSpeaking = true;
      const visemes = ['vowel_a', 'mid', 'wide_e', 'round_o', 'mid'];
      let idx = 0;
      this.visemeTimer = setInterval(() => {
        if (!this.isSpeaking) return;
        this.setViseme(this.activeSpeaker, visemes[idx % visemes.length]);
        idx++;
      }, 140);
    }
    if (this.synth && this.synth.paused) {
      this.synth.resume();
    }
  }

  stop() {
    this.resetMouths();
    if (this.synth) {
      this.synth.cancel();
    }
  }
}

window.SpeechCoordinator = SpeechCoordinator;
