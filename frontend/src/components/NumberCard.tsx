interface Props {
  number: number
  title: string
  subtitle: string
  description: string
  icon: string
  master?: boolean
}

export default function NumberCard({ number, title, subtitle, description, icon, master }: Props) {
  return (
    <div className={`mystic-card rounded-xl border p-5 space-y-3 ${master ? 'border-mystic-gold/40 bg-mystic-gold/5' : 'border-mystic-border bg-mystic-card'}`}>
      <div className="flex items-start justify-between gap-3">
        <div className="flex items-center gap-3">
          <span className="text-xl">{icon}</span>
          <div>
            <p className="text-xs text-mystic-muted uppercase tracking-widest">{title}</p>
            <p className="font-semibold text-mystic-text">{subtitle}</p>
          </div>
        </div>
        <div className={`number-badge rounded-lg px-3 py-1.5 text-center min-w-[52px] ${master ? 'border-mystic-gold/50' : ''}`}>
          <span className={`font-serif text-2xl font-bold ${master ? 'text-mystic-gold glow-gold' : 'text-mystic-purple'}`}>
            {number}
          </span>
          {master && <p className="text-xs text-mystic-gold/70 -mt-0.5">Maître</p>}
        </div>
      </div>
      <p className="text-sm text-mystic-muted leading-relaxed">{description}</p>
    </div>
  )
}
