// Â© 2026 Aboubacar Sidick Meite (ApollonASM8977) â€” All Rights Reserved
import { useState } from 'react'
import { User, Heart } from 'lucide-react'
import ProfileTab from './components/ProfileTab'
import CompatibilityTab from './components/CompatibilityTab'

type Tab = 'profile' | 'compat'

const TABS: { id: Tab; label: string; icon: React.ReactNode }[] = [
  { id: 'profile', label: 'Mon Profil',     icon: <User size={14} /> },
  { id: 'compat',  label: 'CompatibilitÃ©',  icon: <Heart size={14} /> },
]

export default function App() {
  const [tab, setTab] = useState<Tab>('profile')

  return (
    <div className="relative min-h-screen bg-mystic-bg overflow-x-hidden">
      {/* Stars */}
      <div className="stars" />

      {/* Ambient glow */}
      <div className="fixed top-0 left-1/2 -translate-x-1/2 w-96 h-96 bg-mystic-purple/10 rounded-full blur-[100px] pointer-events-none" />
      <div className="fixed bottom-0 right-1/4 w-64 h-64 bg-mystic-gold/8 rounded-full blur-[80px] pointer-events-none" />

      {/* Content */}
      <div className="relative z-10 flex flex-col items-center px-4 py-10 min-h-screen">
        {/* Header */}
        <header className="w-full max-w-lg mb-10 text-center space-y-4">
          <div className="flex items-center justify-center gap-3">
            <span className="text-4xl animate-float">âœ¨</span>
            <h1 className="font-serif text-4xl font-bold gradient-text tracking-wide">
              NumÃ©rologie
            </h1>
            <span className="text-4xl animate-float" style={{ animationDelay: '1s' }}>âœ¨</span>
          </div>
          <p className="text-sm text-mystic-muted tracking-wide">
            DÃ©couvrez les vibrations cachÃ©es de votre prÃ©nom et de votre date de naissance
          </p>
          <div className="flex items-center justify-center gap-2 text-mystic-muted/40 text-xs">
            <span className="w-16 h-px bg-gradient-to-r from-transparent to-mystic-gold/30" />
            Chemin de vie Â· Expression Â· Motivation Â· Cycles
            <span className="w-16 h-px bg-gradient-to-l from-transparent to-mystic-gold/30" />
          </div>
        </header>

        {/* Card */}
        <main className="w-full max-w-lg">
          <div className="rounded-2xl border border-mystic-border bg-mystic-surface shadow-purple">
            {/* Tabs */}
            <div className="flex border-b border-mystic-border">
              {TABS.map(({ id, label, icon }) => (
                <button
                  key={id}
                  onClick={() => setTab(id)}
                  className={`
                    flex-1 flex items-center justify-center gap-2 py-4 text-xs uppercase tracking-widest font-medium
                    transition-all border-b-2 -mb-px
                    ${tab === id
                      ? 'border-mystic-gold text-mystic-gold bg-mystic-gold/5'
                      : 'border-transparent text-mystic-muted hover:text-mystic-text'
                    }
                  `}
                >
                  {icon}
                  {label}
                </button>
              ))}
            </div>

            {/* Content */}
            <div className="p-6">
              {tab === 'profile' && <ProfileTab />}
              {tab === 'compat'  && <CompatibilityTab />}
            </div>
          </div>

          <p className="text-center text-mystic-muted/30 text-xs mt-6 tracking-widest">
            v1.0.0 Â· FastAPI + React Â· Analyse locale
          </p>
          <p className="text-right text-mystic-muted/20 text-xs mt-1 pr-1">Â© ASM</p>
        </main>
      </div>
    </div>
  )
}

