"""
AQUACARD: THE FUTURE OF INTELLIGENT WATER PURIFICATION
Script: generate_svgs.py

Generates professional vector SVG assets:
1. dr_adrian.svg - Dr. Adrian Reynolds (Senior Water Systems & AI Researcher)
2. ethan_carter.svg - Ethan Carter (Junior Embedded AI Researcher with tablet)
3. aquacard_machine.svg - AQUACARD Intelligent Purification Machine
4. lab_background.svg - Futuristic Intelligent Water Lab
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "static", "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# ==============================================================================
# 1. DR. ADRIAN REYNOLDS (SENIOR RESEARCHER) SVG
# ==============================================================================
def create_dr_adrian_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 600" width="320" height="600" id="svg-adrian">
  <defs>
    <linearGradient id="adrian-coat-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14243b" />
      <stop offset="50%" stop-color="#0f1b2d" />
      <stop offset="100%" stop-color="#09121f" />
    </linearGradient>
    <linearGradient id="adrian-skin-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8d5bb" />
      <stop offset="100%" stop-color="#e2ba9b" />
    </linearGradient>
    <linearGradient id="adrian-hair-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2c1a11" />
      <stop offset="100%" stop-color="#150d09" />
    </linearGradient>
    <linearGradient id="badge-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff" />
      <stop offset="100%" stop-color="#0077ff" />
    </linearGradient>
    <filter id="adrian-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <g id="adrian-character" filter="url(#adrian-shadow)">
    <!-- Shadow beneath feet -->
    <ellipse cx="160" cy="580" rx="90" ry="12" fill="#000000" opacity="0.6"/>

    <!-- Legs & Trousers -->
    <g id="adrian-legs">
      <!-- Left leg -->
      <path d="M 125 350 L 115 540 L 145 540 L 150 350 Z" fill="#0b1320"/>
      <!-- Right leg -->
      <path d="M 170 350 L 175 540 L 205 540 L 195 350 Z" fill="#0d1726"/>
      <!-- Left shoe -->
      <path d="M 110 535 L 148 535 L 150 555 L 105 555 Z" fill="#050a12"/>
      <!-- Right shoe -->
      <path d="M 172 535 L 210 535 L 215 555 L 170 555 Z" fill="#050a12"/>
    </g>

    <!-- Torso and Lab Coat -->
    <g id="adrian-torso">
      <!-- Inner Shirt & Tie -->
      <path d="M 142 165 L 178 165 L 172 260 L 148 260 Z" fill="#edf2f7"/>
      <path d="M 158 175 L 162 175 L 164 240 L 156 240 Z" fill="#0088ff"/>
      <polygon points="160,178 165,188 155,188" fill="#0055aa"/>

      <!-- Tailored Navy Lab Coat -->
      <path d="M 110 170 C 130 160, 190 160, 210 170 L 225 380 C 205 400, 115 400, 95 380 Z" fill="url(#adrian-coat-grad)"/>
      <!-- Lapels -->
      <path d="M 128 165 L 145 250 L 132 255 L 118 172 Z" fill="#1c304d"/>
      <path d="M 192 165 L 175 250 L 188 255 L 202 172 Z" fill="#1c304d"/>

      <!-- Smart ID Badge -->
      <rect x="180" y="210" width="28" height="38" rx="3" fill="#0a1626" stroke="#00e5ff" stroke-width="1.2"/>
      <rect x="184" y="215" width="20" height="14" fill="#00e5ff" opacity="0.3"/>
      <circle cx="194" cy="222" r="4" fill="#ffffff"/>
      <rect x="184" y="233" width="20" height="2" fill="#00e5ff"/>
      <rect x="184" y="238" width="14" height="2" fill="#94a3b8"/>

      <!-- Pocket and Pen -->
      <line x1="122" y1="230" x2="140" y2="230" stroke="#253e61" stroke-width="2"/>
      <line x1="126" y1="224" x2="126" y2="233" stroke="#00e5ff" stroke-width="1.5"/>
    </g>

    <!-- Head and Neck -->
    <g id="adrian-head-group">
      <!-- Neck -->
      <path d="M 148 140 L 172 140 L 174 170 L 146 170 Z" fill="url(#adrian-skin-grad)"/>
      <path d="M 146 160 L 160 170 L 174 160" fill="none" stroke="#cf9f7e" stroke-width="1.5"/>

      <!-- Head Base -->
      <path d="M 130 90 C 130 45, 190 45, 190 90 C 190 135, 175 155, 160 155 C 145 155, 130 135, 130 90 Z" fill="url(#adrian-skin-grad)"/>

      <!-- Ears -->
      <ellipse cx="128" cy="98" rx="6" ry="10" fill="url(#adrian-skin-grad)"/>
      <ellipse cx="192" cy="98" rx="6" ry="10" fill="url(#adrian-skin-grad)"/>

      <!-- Hair (Short styled dark professional) -->
      <path d="M 127 82 C 127 50, 145 35, 160 35 C 178 35, 195 50, 193 82 C 185 65, 165 60, 150 64 C 138 68, 132 75, 127 82 Z" fill="url(#adrian-hair-grad)"/>
      <path d="M 127 82 L 129 98 L 134 94 L 132 80 Z" fill="url(#adrian-hair-grad)"/>
      <path d="M 193 82 L 191 98 L 186 94 L 188 80 Z" fill="url(#adrian-hair-grad)"/>

      <!-- Groomed Beard & Stubble -->
      <path d="M 135 105 C 140 148, 180 148, 185 105 C 180 125, 140 125, 135 105 Z" fill="#25160e" opacity="0.6"/>

      <!-- Eyebrows -->
      <path d="M 138 78 Q 148 74 154 78" stroke="#1f1109" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <path d="M 166 78 Q 172 74 182 78" stroke="#1f1109" stroke-width="2.5" fill="none" stroke-linecap="round"/>

      <!-- Eyes & Blinking mechanism -->
      <g id="adrian-eyes">
        <!-- Sclera -->
        <ellipse cx="146" cy="88" rx="6" ry="3.5" fill="#ffffff"/>
        <ellipse cx="174" cy="88" rx="6" ry="3.5" fill="#ffffff"/>
        <!-- Iris -->
        <circle cx="147" cy="88" r="2.4" fill="#2c1a11"/>
        <circle cx="175" cy="88" r="2.4" fill="#2c1a11"/>
        <circle cx="147.8" cy="87.2" r="0.8" fill="#ffffff"/>
        <circle cx="175.8" cy="87.2" r="0.8" fill="#ffffff"/>
        <!-- Eyelid for blinking (scales Y to 0 or closes) -->
        <path id="adrian-blink" d="M 139 88 Q 146 84 153 88 M 167 88 Q 174 84 181 88" stroke="#cf9f7e" stroke-width="1.8" fill="none" opacity="0"/>
      </g>

      <!-- Nose -->
      <path d="M 158 84 L 162 100 L 157 103 L 163 103" stroke="#c08d6c" stroke-width="1.8" fill="none" stroke-linecap="round"/>

      <!-- Mouth Group with 5 Visemes -->
      <g id="adrian-mouth-group">
        <!-- 1. Rest mouth -->
        <path id="adrian-mouth-rest" d="M 152 118 Q 160 120 168 118" stroke="#873e23" stroke-width="2.2" fill="none" stroke-linecap="round" />
        <!-- 2. Vowel A mouth (open) -->
        <ellipse id="adrian-mouth-vowel-a" cx="160" cy="120" rx="6.5" ry="5.5" fill="#4a1515" stroke="#873e23" stroke-width="1.8" style="display:none;" />
        <!-- 3. Round O mouth -->
        <ellipse id="adrian-mouth-round-o" cx="160" cy="120" rx="4.5" ry="5.5" fill="#4a1515" stroke="#873e23" stroke-width="1.8" style="display:none;" />
        <!-- 4. Wide E mouth -->
        <path id="adrian-mouth-wide-e" d="M 150 118 Q 160 115 170 118 Q 160 124 150 118 Z" fill="#ffffff" stroke="#873e23" stroke-width="1.8" style="display:none;" />
        <!-- 5. Mid mouth -->
        <ellipse id="adrian-mouth-mid" cx="160" cy="119" rx="5.5" ry="3.2" fill="#4a1515" stroke="#873e23" stroke-width="1.8" style="display:none;" />
      </g>
    </g>

    <!-- Arms & Hands -->
    <!-- Left Arm (Explaining / Welcoming gesture) -->
    <g id="adrian-arm-left">
      <path d="M 110 178 L 80 260 L 60 330" stroke="#0f1b2d" stroke-width="22" stroke-linecap="round" fill="none"/>
      <!-- Hand -->
      <ellipse cx="58" cy="336" rx="9" ry="12" fill="url(#adrian-skin-grad)" transform="rotate(-15 58 336)"/>
      <path d="M 52 330 Q 42 342 56 348" stroke="#cf9f7e" stroke-width="2" fill="none"/>
    </g>

    <!-- Right Arm (Pointing / Highlighting gesture) -->
    <g id="adrian-arm-right">
      <path id="adrian-arm-right-path" d="M 210 178 L 240 250 L 270 240" stroke="#0f1b2d" stroke-width="22" stroke-linecap="round" fill="none"/>
      <!-- Pointing Hand -->
      <g id="adrian-hand-right" transform="translate(265, 230)">
        <ellipse cx="10" cy="10" rx="9" ry="9" fill="url(#adrian-skin-grad)"/>
        <!-- Index finger pointing -->
        <path d="M 16 8 L 34 5" stroke="#e2ba9b" stroke-width="4.5" stroke-linecap="round"/>
      </g>
    </g>
  </g>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "dr_adrian.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved dr_adrian.svg")

# ==============================================================================
# 2. ETHAN CARTER (JUNIOR RESEARCHER) SVG
# ==============================================================================
def create_ethan_carter_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 600" width="320" height="600" id="svg-ethan">
  <defs>
    <linearGradient id="ethan-shirt-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e56a0" />
      <stop offset="50%" stop-color="#163172" />
      <stop offset="100%" stop-color="#0e1d42" />
    </linearGradient>
    <linearGradient id="ethan-skin-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fbe4d0" />
      <stop offset="100%" stop-color="#e9caa8" />
    </linearGradient>
    <linearGradient id="ethan-hair-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#5a331c" />
      <stop offset="100%" stop-color="#2d170b" />
    </linearGradient>
    <linearGradient id="tablet-holo-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#0077ff" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#001a40" stop-opacity="0.9" />
    </linearGradient>
    <filter id="ethan-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <g id="ethan-character" filter="url(#ethan-shadow)">
    <!-- Shadow beneath feet -->
    <ellipse cx="160" cy="580" rx="85" ry="12" fill="#000000" opacity="0.6"/>

    <!-- Legs & Chinos -->
    <g id="ethan-legs">
      <!-- Left leg -->
      <path d="M 128 350 L 120 540 L 148 540 L 152 350 Z" fill="#1b2432"/>
      <!-- Right leg -->
      <path d="M 168 350 L 172 540 L 200 540 L 192 350 Z" fill="#202b3c"/>
      <!-- Left shoe (modern sneakers) -->
      <path d="M 115 536 L 150 536 L 152 555 L 110 555 Z" fill="#334155"/>
      <path d="M 110 552 L 152 552 L 152 556 L 110 556 Z" fill="#00e5ff"/>
      <!-- Right shoe -->
      <path d="M 168 536 L 204 536 L 208 555 L 165 555 Z" fill="#334155"/>
      <path d="M 165 552 L 208 552 L 208 556 L 165 556 Z" fill="#00e5ff"/>
    </g>

    <!-- Torso and Cobalt-Blue Shirt -->
    <g id="ethan-torso">
      <!-- Smart Casual Blue Shirt -->
      <path d="M 116 172 C 132 165, 188 165, 204 172 L 214 360 C 195 368, 125 368, 106 360 Z" fill="url(#ethan-shirt-grad)"/>
      <!-- Collar -->
      <polygon points="144,168 160,192 136,182" fill="#2b6cb0"/>
      <polygon points="176,168 160,192 184,182" fill="#2b6cb0"/>
      <!-- Button Placket -->
      <line x1="160" y1="192" x2="160" y2="355" stroke="#122754" stroke-width="2.5"/>
      <circle cx="160" cy="215" r="2" fill="#93c5fd"/>
      <circle cx="160" cy="250" r="2" fill="#93c5fd"/>
      <circle cx="160" cy="285" r="2" fill="#93c5fd"/>

      <!-- High-Tech Wrist Telemetry Link -->
      <rect x="94" y="278" width="16" height="12" rx="2" fill="#0f172a" stroke="#00e5ff" stroke-width="1.2"/>
      <circle cx="102" cy="284" r="2" fill="#00e5ff"/>
    </g>

    <!-- Head and Neck -->
    <g id="ethan-head-group">
      <!-- Neck -->
      <path d="M 150 144 L 170 144 L 172 172 L 148 172 Z" fill="url(#ethan-skin-grad)"/>

      <!-- Head Base (Youthful, clean jawline) -->
      <path d="M 132 94 C 132 50, 188 50, 188 94 C 188 135, 172 154, 160 154 C 148 154, 132 135, 132 94 Z" fill="url(#ethan-skin-grad)"/>

      <!-- Ears -->
      <ellipse cx="130" cy="98" rx="5.5" ry="9" fill="url(#ethan-skin-grad)"/>
      <ellipse cx="190" cy="98" rx="5.5" ry="9" fill="url(#ethan-skin-grad)"/>

      <!-- Hair (Youthful chestnut brown layered) -->
      <path d="M 128 86 C 128 48, 146 36, 160 36 C 176 36, 192 48, 192 86 C 185 70, 168 62, 155 65 C 142 68, 135 76, 128 86 Z" fill="url(#ethan-hair-grad)"/>
      <!-- Soft sideburns -->
      <path d="M 128 86 L 131 100 L 134 96 Z" fill="url(#ethan-hair-grad)"/>
      <path d="M 192 86 L 189 100 L 186 96 Z" fill="url(#ethan-hair-grad)"/>

      <!-- Eyebrows (Curious, inquisitive) -->
      <path d="M 139 79 Q 148 76 154 80" stroke="#3b2010" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      <path d="M 166 80 Q 172 76 181 79" stroke="#3b2010" stroke-width="2.2" fill="none" stroke-linecap="round"/>

      <!-- Eyes (Hazel, expressive) -->
      <g id="ethan-eyes">
        <ellipse cx="146" cy="89" rx="6" ry="3.8" fill="#ffffff"/>
        <ellipse cx="174" cy="89" rx="6" ry="3.8" fill="#ffffff"/>
        <circle cx="147" cy="89" r="2.5" fill="#5a381e"/>
        <circle cx="175" cy="89" r="2.5" fill="#5a381e"/>
        <circle cx="147.8" cy="88.2" r="0.9" fill="#ffffff"/>
        <circle cx="175.8" cy="88.2" r="0.9" fill="#ffffff"/>
        <!-- Eyelid blink line -->
        <path id="ethan-blink" d="M 139 89 Q 146 85 153 89 M 167 89 Q 174 85 181 89" stroke="#cf9f7e" stroke-width="1.8" fill="none" opacity="0"/>
      </g>

      <!-- Nose -->
      <path d="M 159 86 L 161 101 L 157 104 L 163 104" stroke="#c08d6c" stroke-width="1.7" fill="none" stroke-linecap="round"/>

      <!-- Mouth Group with 5 Visemes -->
      <g id="ethan-mouth-group">
        <!-- 1. Rest mouth -->
        <path id="ethan-mouth-rest" d="M 153 120 Q 160 122 167 120" stroke="#873e23" stroke-width="2.0" fill="none" stroke-linecap="round" />
        <!-- 2. Vowel A mouth -->
        <ellipse id="ethan-mouth-vowel-a" cx="160" cy="121" rx="6.0" ry="5.2" fill="#4a1515" stroke="#873e23" stroke-width="1.8" style="display:none;" />
        <!-- 3. Round O mouth -->
        <ellipse id="ethan-mouth-round-o" cx="160" cy="121" rx="4.2" ry="5.2" fill="#4a1515" stroke="#873e23" stroke-width="1.8" style="display:none;" />
        <!-- 4. Wide E mouth -->
        <path id="ethan-mouth-wide-e" d="M 151 119 Q 160 116 169 119 Q 160 124 151 119 Z" fill="#ffffff" stroke="#873e23" stroke-width="1.8" style="display:none;" />
        <!-- 5. Mid mouth -->
        <ellipse id="ethan-mouth-mid" cx="160" cy="120" rx="5.2" ry="3.0" fill="#4a1515" stroke="#873e23" stroke-width="1.8" style="display:none;" />
      </g>
    </g>

    <!-- Arms & Holographic Diagnostic Tablet -->
    <!-- Left Arm holding tablet -->
    <g id="ethan-arm-left">
      <path d="M 116 182 L 95 260 L 130 295" stroke="#163172" stroke-width="20" stroke-linecap="round" fill="none"/>
      <!-- Hand holding edge of tablet -->
      <circle cx="132" cy="298" r="8" fill="url(#ethan-skin-grad)"/>
    </g>

    <!-- Holographic Diagnostic Tablet -->
    <g id="ethan-tablet" transform="translate(110, 240)">
      <!-- Glass tablet base -->
      <rect x="0" y="0" width="105" height="75" rx="6" fill="url(#tablet-holo-grad)" stroke="#00e5ff" stroke-width="1.8" filter="drop-shadow(0 0 8px #00e5ff88)"/>
      <!-- Tablet HUD Content -->
      <text x="8" y="14" fill="#ffffff" font-size="7" font-family="monospace" font-weight="bold">AQUACARD TELEMETRY</text>
      <text x="8" y="26" fill="#00e5ff" font-size="6" font-family="monospace">pH: 7.32 | TURB: 0.38</text>
      <text x="8" y="36" fill="#38bdf8" font-size="6" font-family="monospace">TDS: 52ppm | Q: 4.2L</text>
      <!-- Mini waveform chart -->
      <path d="M 8 58 L 22 52 L 35 60 L 50 48 L 68 55 L 85 45 L 98 52" stroke="#00e5ff" stroke-width="1.5" fill="none"/>
      <circle cx="98" cy="52" r="2.5" fill="#00e676"/>
      <!-- Diagnostic status pill -->
      <rect x="8" y="62" width="45" height="8" rx="2" fill="#00e676" opacity="0.3"/>
      <text x="12" y="68" fill="#00e676" font-size="5" font-family="sans-serif" font-weight="bold">AI: OPTIMAL PATH</text>
    </g>

    <!-- Right Arm interacting with tablet / gesturing -->
    <g id="ethan-arm-right">
      <path id="ethan-arm-right-path" d="M 204 182 L 225 250 L 195 270" stroke="#163172" stroke-width="20" stroke-linecap="round" fill="none"/>
      <!-- Right hand touching tablet screen -->
      <circle cx="193" cy="272" r="8" fill="url(#ethan-skin-grad)"/>
      <circle cx="188" cy="270" r="3" fill="#00e5ff" opacity="0.8"/>
    </g>
  </g>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "ethan_carter.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved ethan_carter.svg")

# ==============================================================================
# 3. AQUACARD MACHINE SVG
# ==============================================================================
def create_aquacard_machine_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 650" width="900" height="650" id="svg-aquacard">
  <defs>
    <!-- Gradients for Machine Frame -->
    <linearGradient id="chassis-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="50%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="metal-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="50%" stop-color="#64748b" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>

    <!-- Chamber Glass & Water Gradients -->
    <linearGradient id="chamber-glass" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.25" />
      <stop offset="20%" stop-color="#00e5ff" stop-opacity="0.08" />
      <stop offset="80%" stop-color="#0077ff" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.3" />
    </linearGradient>

    <!-- Fluid Color Gradients (Turbid Raw to Pure Aqua) -->
    <linearGradient id="water-raw" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#a3824c" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#785d32" stop-opacity="0.85" />
    </linearGradient>
    <linearGradient id="water-sediment" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#6ba2a8" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#40808a" stop-opacity="0.8" />
    </linearGradient>
    <linearGradient id="water-carbon" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.85" />
    </linearGradient>
    <linearGradient id="water-pure" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#00b4d8" stop-opacity="0.95" />
    </linearGradient>

    <!-- UV Glow -->
    <filter id="uv-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Machine Stand and Shadow -->
  <ellipse cx="450" cy="620" rx="410" ry="22" fill="#000000" opacity="0.6"/>

  <!-- Main Industrial Chassis Base -->
  <rect x="50" y="520" width="800" height="85" rx="10" fill="url(#chassis-grad)" stroke="#38bdf8" stroke-width="1.8"/>
  <rect x="70" y="535" width="760" height="15" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <!-- Status LEDs on Base -->
  <circle cx="95" cy="542" r="4" fill="#00e676"/>
  <text x="110" y="546" fill="#94a3b8" font-size="10" font-family="monospace">PUMP A: ACTIVE (4.2 L/min)</text>
  <circle cx="320" cy="542" r="4" fill="#00e5ff"/>
  <text x="335" y="546" fill="#94a3b8" font-size="10" font-family="monospace">MEMBRANE ΔP: 2.1 psi</text>
  <circle cx="560" cy="542" r="4" fill="#a855f7"/>
  <text x="575" y="546" fill="#94a3b8" font-size="10" font-family="monospace">UV REACTOR: 254nm (42 mJ/cm²)</text>
  <rect x="70" y="565" width="760" height="28" rx="4" fill="#070d18" stroke="#00e5ff" stroke-width="1"/>
  <text x="450" y="583" fill="#00e5ff" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="3">AQUACARD INTELLIGENT PURIFICATION PLATFORM — Mk IV</text>

  <!-- Top Manifold Bracket -->
  <rect x="50" y="60" width="800" height="40" rx="8" fill="url(#chassis-grad)" stroke="#38bdf8" stroke-width="1.8"/>
  <rect x="80" y="72" width="740" height="16" rx="4" fill="#091322"/>
  <text x="95" y="84" fill="#38bdf8" font-size="11" font-family="monospace" font-weight="bold">CLOSED-LOOP DIAGNOSTIC BUS: REAL-TIME FLUIDIC TELEMETRY</text>

  <!-- Side Structural Pillars -->
  <rect x="50" y="98" width="30" height="424" fill="url(#metal-accent)" stroke="#475569" stroke-width="1"/>
  <rect x="820" y="98" width="30" height="424" fill="url(#metal-accent)" stroke="#475569" stroke-width="1"/>

  <!-- ===================================================================== -->
  <!-- 5 TRANSPARENT PURIFICATION CHAMBERS                                   -->
  <!-- ===================================================================== -->

  <!-- CHAMBER 1: Raw Water Input & Sensor Manifold (x=110 to 220) -->
  <g id="chamber-1-input">
    <!-- Tube Base and Cap -->
    <rect x="110" y="95" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="110" y="475" width="110" height="20" rx="4" fill="#475569"/>
    <!-- Outer Glass Cylinder -->
    <rect x="115" y="115" width="100" height="360" rx="6" fill="#071729" stroke="#334155" stroke-width="1.5"/>
    <!-- Fluid Inflow (Turbid Raw Water) -->
    <rect id="fluid-raw" x="118" y="140" width="94" height="332" rx="4" fill="url(#water-raw)"/>
    <!-- Glass Reflection Highlight -->
    <rect x="115" y="115" width="100" height="360" rx="6" fill="url(#chamber-glass)"/>

    <!-- Sensor Probes Immersed in Chamber 1 -->
    <g id="sensors-chamber-1">
      <!-- pH Probe -->
      <line x1="135" y1="95" x2="135" y2="260" stroke="#00e5ff" stroke-width="3"/>
      <circle cx="135" cy="260" r="5" fill="#00e5ff"/>
      <text x="125" y="145" fill="#ffffff" font-size="8" font-family="monospace">pH</text>

      <!-- Turbidity Nephelometer Probe -->
      <line x1="165" y1="95" x2="165" y2="300" stroke="#ffb300" stroke-width="3"/>
      <circle cx="165" cy="300" r="6" fill="#ffb300"/>
      <text x="155" y="170" fill="#ffffff" font-size="8" font-family="monospace">TURB</text>

      <!-- TDS & Conductivity Probe -->
      <line x1="195" y1="95" x2="195" y2="340" stroke="#00e676" stroke-width="3"/>
      <circle cx="195" cy="340" r="5" fill="#00e676"/>
      <text x="187" y="195" fill="#ffffff" font-size="8" font-family="monospace">TDS</text>
    </g>

    <!-- Chamber 1 Label -->
    <rect x="115" y="498" width="100" height="18" rx="3" fill="#0a182c" stroke="#ffb300" stroke-width="1"/>
    <text x="165" y="511" fill="#ffb300" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">1. SENSOR MANIFOLD</text>
  </g>

  <!-- INTER-STAGE PIPE 1-2 with Flow Particles -->
  <path d="M 215 450 L 260 450" stroke="#00e5ff" stroke-width="8" fill="none" opacity="0.8"/>

  <!-- CHAMBER 2: Sediment Filter (x=260 to 370) -->
  <g id="chamber-2-sediment">
    <rect x="260" y="95" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="260" y="475" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="265" y="115" width="100" height="360" rx="6" fill="#071729" stroke="#334155" stroke-width="1.5"/>
    <!-- Fluid -->
    <rect x="268" y="130" width="94" height="342" rx="4" fill="url(#water-sediment)"/>
    <!-- Polypropylene Filter Core -->
    <rect x="285" y="130" width="60" height="342" rx="4" fill="#e2e8f0" opacity="0.9" stroke="#94a3b8" stroke-width="1"/>
    <!-- Wound Filter Grooves -->
    <line x1="285" y1="170" x2="345" y2="170" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="285" y1="210" x2="345" y2="210" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="285" y1="250" x2="345" y2="250" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="285" y1="290" x2="345" y2="290" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="285" y1="330" x2="345" y2="330" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="285" y1="370" x2="345" y2="370" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="285" y1="410" x2="345" y2="410" stroke="#cbd5e1" stroke-width="2"/>
    <!-- Trapped Silt/Particulate Specks -->
    <circle cx="275" cy="220" r="2.5" fill="#785d32"/>
    <circle cx="278" cy="310" r="3" fill="#785d32"/>
    <circle cx="352" cy="270" r="2" fill="#785d32"/>
    <!-- Glass Highlight -->
    <rect x="265" y="115" width="100" height="360" rx="6" fill="url(#chamber-glass)"/>

    <rect x="265" y="498" width="100" height="18" rx="3" fill="#0a182c" stroke="#38bdf8" stroke-width="1"/>
    <text x="315" y="511" fill="#38bdf8" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">2. SEDIMENT (5µm)</text>
  </g>

  <!-- INTER-STAGE PIPE 2-3 -->
  <path d="M 365 140 L 410 140" stroke="#38bdf8" stroke-width="8" fill="none" opacity="0.8"/>

  <!-- CHAMBER 3: Activated Carbon Cartridge (x=410 to 520) -->
  <g id="chamber-3-carbon">
    <rect x="410" y="95" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="410" y="475" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="415" y="115" width="100" height="360" rx="6" fill="#071729" stroke="#334155" stroke-width="1.5"/>
    <!-- Fluid -->
    <rect x="418" y="130" width="94" height="342" rx="4" fill="url(#water-carbon)"/>
    <!-- Extruded Carbon Block Matrix (Dark Granular) -->
    <rect x="435" y="130" width="60" height="342" rx="4" fill="#18181b" stroke="#27272a" stroke-width="1.5"/>
    <!-- Carbon Pores pattern -->
    <circle cx="450" cy="180" r="2" fill="#3f3f46"/>
    <circle cx="475" cy="220" r="2" fill="#3f3f46"/>
    <circle cx="455" cy="270" r="2" fill="#3f3f46"/>
    <circle cx="480" cy="330" r="2" fill="#3f3f46"/>
    <circle cx="445" cy="390" r="2" fill="#3f3f46"/>
    <!-- Chlorine adsorption glow -->
    <rect x="435" y="130" width="60" height="342" rx="4" fill="#00e5ff" opacity="0.1"/>
    <!-- Glass Highlight -->
    <rect x="415" y="115" width="100" height="360" rx="6" fill="url(#chamber-glass)"/>

    <rect x="415" y="498" width="100" height="18" rx="3" fill="#0a182c" stroke="#38bdf8" stroke-width="1"/>
    <text x="465" y="511" fill="#38bdf8" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">3. ACTIVE CARBON</text>
  </g>

  <!-- INTER-STAGE PIPE 3-4 with AI Motorized 3-Way Proportional Valve -->
  <path d="M 515 450 L 560 450" stroke="#00e5ff" stroke-width="8" fill="none" opacity="0.8"/>
  <!-- Valve Widget -->
  <circle cx="538" cy="450" r="10" fill="#0f172a" stroke="#00e5ff" stroke-width="2"/>
  <polygon points="534,444 544,450 534,456" fill="#00e5ff"/>

  <!-- CHAMBER 4: Dynamic RO / UF Membrane Vessel (x=560 to 670) -->
  <g id="chamber-4-membrane">
    <rect x="560" y="95" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="560" y="475" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="565" y="115" width="100" height="360" rx="6" fill="#071729" stroke="#334155" stroke-width="1.5"/>
    <!-- Pure Water Fluid -->
    <rect x="568" y="130" width="94" height="342" rx="4" fill="url(#water-pure)"/>
    <!-- Spiral Wound TFC Membrane Vessel -->
    <rect x="585" y="130" width="60" height="342" rx="20" fill="#0284c7" opacity="0.75" stroke="#38bdf8" stroke-width="1.5"/>
    <!-- Spiral Membrane Wraps -->
    <ellipse cx="615" cy="180" rx="25" ry="8" fill="none" stroke="#bae6fd" stroke-width="1.5"/>
    <ellipse cx="615" cy="240" rx="25" ry="8" fill="none" stroke="#bae6fd" stroke-width="1.5"/>
    <ellipse cx="615" cy="300" rx="25" ry="8" fill="none" stroke="#bae6fd" stroke-width="1.5"/>
    <ellipse cx="615" cy="360" rx="25" ry="8" fill="none" stroke="#bae6fd" stroke-width="1.5"/>
    <ellipse cx="615" cy="420" rx="25" ry="8" fill="none" stroke="#bae6fd" stroke-width="1.5"/>
    <!-- Glass Highlight -->
    <rect x="565" y="115" width="100" height="360" rx="6" fill="url(#chamber-glass)"/>

    <rect x="565" y="498" width="100" height="18" rx="3" fill="#0a182c" stroke="#00e5ff" stroke-width="1"/>
    <text x="615" y="511" fill="#00e5ff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">4. RO / UF MEMBRANE</text>
  </g>

  <!-- INTER-STAGE PIPE 4-5 -->
  <path d="M 665 140 L 710 140" stroke="#00e5ff" stroke-width="8" fill="none" opacity="0.9"/>

  <!-- CHAMBER 5: Germicidal UV Disinfection Photoreactor (x=710 to 820) -->
  <g id="chamber-5-uv">
    <rect x="710" y="95" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="710" y="475" width="110" height="20" rx="4" fill="#475569"/>
    <rect x="715" y="115" width="100" height="360" rx="6" fill="#071729" stroke="#334155" stroke-width="1.5"/>
    <!-- Crystal Pure Fluid with UV Luminescence -->
    <rect x="718" y="130" width="94" height="342" rx="4" fill="url(#water-pure)"/>
    <!-- Intense 254nm Ultraviolet Radiant Core -->
    <rect x="750" y="130" width="30" height="342" rx="10" fill="#a855f7" filter="url(#uv-glow)" opacity="0.85"/>
    <rect x="756" y="130" width="18" height="342" rx="6" fill="#f3e8ff" opacity="0.95"/>
    <!-- Photolytic Radiation Rays -->
    <line x1="740" y1="200" x2="725" y2="200" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="790" y1="200" x2="805" y2="200" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="740" y1="280" x2="725" y2="280" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="790" y1="280" x2="805" y2="280" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="740" y1="360" x2="725" y2="360" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="790" y1="360" x2="805" y2="360" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,3"/>
    <!-- Glass Highlight -->
    <rect x="715" y="115" width="100" height="360" rx="6" fill="url(#chamber-glass)"/>

    <rect x="715" y="498" width="100" height="18" rx="3" fill="#0a182c" stroke="#a855f7" stroke-width="1"/>
    <text x="765" y="511" fill="#c084fc" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">5. UV REACTOR (254nm)</text>
  </g>

  <!-- Clean Water Outlet Pipe & Flow Valve -->
  <path d="M 815 450 L 865 450 L 865 490" stroke="#00e5ff" stroke-width="10" fill="none"/>
  <polygon points="860,490 870,490 865,502" fill="#00e5ff"/>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "aquacard_machine.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved aquacard_machine.svg")

# ==============================================================================
# 4. FUTURISTIC LAB BACKGROUND SVG
# ==============================================================================
def create_lab_background_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080" id="svg-lab-bg">
  <defs>
    <!-- Laboratory Ambient Gradient -->
    <linearGradient id="lab-wall-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#020617" />
      <stop offset="40%" stop-color="#060f1e" />
      <stop offset="70%" stop-color="#0b1b33" />
      <stop offset="100%" stop-color="#030816" />
    </linearGradient>

    <!-- Floor Perspective Gradient -->
    <linearGradient id="floor-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#081426" />
      <stop offset="50%" stop-color="#0a182e" />
      <stop offset="100%" stop-color="#030712" />
    </linearGradient>

    <!-- Cyan Neon Glow -->
    <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="1.0" />
      <stop offset="100%" stop-color="#0077ff" stop-opacity="0.8" />
    </linearGradient>

    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Deep Lab Back Wall -->
  <rect x="0" y="0" width="1920" height="740" fill="url(#lab-wall-grad)"/>

  <!-- Acoustic Modular Panels on Wall -->
  <g id="wall-panels" opacity="0.35">
    <rect x="80" y="80" width="380" height="580" rx="8" fill="#0d1b30" stroke="#1e293b" stroke-width="2"/>
    <rect x="500" y="80" width="920" height="580" rx="8" fill="#0a172a" stroke="#1e293b" stroke-width="2"/>
    <rect x="1460" y="80" width="380" height="580" rx="8" fill="#0d1b30" stroke="#1e293b" stroke-width="2"/>
  </g>

  <!-- Overhead Architectural Light Ribs -->
  <line x1="80" y1="80" x2="1840" y2="80" stroke="url(#neon-cyan)" stroke-width="3" filter="url(#soft-glow)"/>
  <line x1="80" y1="660" x2="1840" y2="660" stroke="#00e5ff" stroke-width="2" opacity="0.6"/>

  <!-- Vertical Neon Pillars -->
  <line x1="80" y1="80" x2="80" y2="660" stroke="#0077ff" stroke-width="2" opacity="0.5"/>
  <line x1="480" y1="80" x2="480" y2="660" stroke="#00e5ff" stroke-width="1.5" opacity="0.4"/>
  <line x1="1440" y1="80" x2="1440" y2="660" stroke="#00e5ff" stroke-width="1.5" opacity="0.4"/>
  <line x1="1840" y1="80" x2="1840" y2="660" stroke="#0077ff" stroke-width="2" opacity="0.5"/>

  <!-- High-Tech Laboratory Floor -->
  <polygon points="0,740 1920,740 1920,1080 0,1080" fill="url(#floor-grad)"/>

  <!-- Floor Grid Perspective Lines -->
  <g id="floor-grid" opacity="0.25">
    <line x1="960" y1="740" x2="960" y2="1080" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="960" y1="740" x2="400" y2="1080" stroke="#38bdf8" stroke-width="1.2"/>
    <line x1="960" y1="740" x2="0" y2="1080" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="960" y1="740" x2="1520" y2="1080" stroke="#38bdf8" stroke-width="1.2"/>
    <line x1="960" y1="740" x2="1920" y2="1080" stroke="#38bdf8" stroke-width="1.5"/>

    <line x1="0" y1="790" x2="1920" y2="790" stroke="#38bdf8" stroke-width="1"/>
    <line x1="0" y1="860" x2="1920" y2="860" stroke="#38bdf8" stroke-width="1.2"/>
    <line x1="0" y1="950" x2="1920" y2="950" stroke="#38bdf8" stroke-width="1.5"/>
  </g>

  <!-- Left Holographic Diagnostic Station (Water Quality Sensor Array) -->
  <g id="left-holo-station" transform="translate(100, 120)">
    <rect x="0" y="0" width="340" height="240" rx="8" fill="#061224" stroke="#00e5ff" stroke-width="1.5" opacity="0.85"/>
    <text x="20" y="30" fill="#00e5ff" font-size="14" font-family="monospace" font-weight="bold">INCOMING TELEMETRY ARRAY</text>
    <line x1="20" y1="40" x2="320" y2="40" stroke="#00e5ff" stroke-width="1" opacity="0.5"/>

    <!-- Sensor Metrics Grid -->
    <text x="20" y="65" fill="#94a3b8" font-size="11" font-family="monospace">pH Level:       7.32 (Nominal)</text>
    <text x="20" y="90" fill="#94a3b8" font-size="11" font-family="monospace">Turbidity:      0.38 NTU</text>
    <text x="20" y="115" fill="#94a3b8" font-size="11" font-family="monospace">Total Dissolved:52 ppm (RO active)</text>
    <text x="20" y="140" fill="#94a3b8" font-size="11" font-family="monospace">Conductivity:   88.0 uS/cm</text>
    <text x="20" y="165" fill="#94a3b8" font-size="11" font-family="monospace">Temperature:    22.1 °C</text>
    <text x="20" y="190" fill="#94a3b8" font-size="11" font-family="monospace">Flow Rate:      4.2 L/min</text>

    <!-- Status pill -->
    <rect x="20" y="205" width="300" height="22" rx="4" fill="#00e676" opacity="0.2"/>
    <text x="170" y="220" fill="#00e676" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">STATUS: MULTI-STAGE PURIFICATION NOMINAL</text>
  </g>

  <!-- Right Holographic Diagnostic Station (MATLAB & AI Decision Engine) -->
  <g id="right-holo-station" transform="translate(1480, 120)">
    <rect x="0" y="0" width="340" height="240" rx="8" fill="#061224" stroke="#38bdf8" stroke-width="1.5" opacity="0.85"/>
    <text x="20" y="30" fill="#38bdf8" font-size="14" font-family="monospace" font-weight="bold">AI PURIFICATION ENGINE</text>
    <line x1="20" y1="40" x2="320" y2="40" stroke="#38bdf8" stroke-width="1" opacity="0.5"/>

    <text x="20" y="65" fill="#cbd5e1" font-size="11" font-family="monospace">CLASSIFIER: Supervised k-NN (k=5)</text>
    <text x="20" y="90" fill="#cbd5e1" font-size="11" font-family="monospace">ACCURACY:   95.83% (Verified)</text>
    <text x="20" y="115" fill="#cbd5e1" font-size="11" font-family="monospace">SEDIMENT:   99.1% Retention</text>
    <text x="20" y="140" fill="#cbd5e1" font-size="11" font-family="monospace">MEMBRANE:   92.4% Rejection</text>
    <text x="20" y="165" fill="#cbd5e1" font-size="11" font-family="monospace">UV EXPOSURE:42 mJ/cm² (254nm)</text>

    <rect x="20" y="205" width="300" height="22" rx="4" fill="#00e5ff" opacity="0.2"/>
    <text x="170" y="220" fill="#00e5ff" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">MATLAB AquaCard.m COMPUTED BASELINE</text>
  </g>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "lab_background.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved lab_background.svg")

if __name__ == "__main__":
    print("[AQUACARD] Generating Vector SVG Assets...")
    create_dr_adrian_svg()
    create_ethan_carter_svg()
    create_aquacard_machine_svg()
    create_lab_background_svg()
    print("[AQUACARD] All Vector SVG Assets Created!")
