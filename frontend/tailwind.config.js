/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        mystic: {
          bg:      '#0a0812',
          surface: '#120e1c',
          card:    '#1a1428',
          border:  '#2d2050',
          gold:    '#f0c040',
          'gold-dim': '#b8902a',
          purple:  '#9b59ff',
          'purple-dim': '#6b3bbf',
          rose:    '#ff6eb4',
          teal:    '#40e0d0',
          text:    '#e8deff',
          muted:   '#7a6aaa',
        },
      },
      fontFamily: {
        sans:  ['"Inter"', 'system-ui', 'sans-serif'],
        serif: ['"Cinzel"', '"Playfair Display"', 'Georgia', 'serif'],
        mono:  ['"JetBrains Mono"', 'Consolas', 'monospace'],
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'shimmer': 'shimmer 2s linear infinite',
        'pulse-gold': 'pulse-gold 3s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%':      { transform: 'translateY(-6px)' },
        },
        shimmer: {
          '0%':   { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        },
        'pulse-gold': {
          '0%, 100%': { opacity: '1', textShadow: '0 0 10px #f0c04080' },
          '50%':      { opacity: '0.7', textShadow: '0 0 20px #f0c040cc' },
        },
      },
      boxShadow: {
        'gold':   '0 0 20px #f0c04033',
        'purple': '0 0 20px #9b59ff33',
      },
    },
  },
  plugins: [],
}
