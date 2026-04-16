import NumberCard from './NumberCard'
import { Star, RotateCcw } from 'lucide-react'

interface Interpretation {
  valeur: number
  title: string
  text: string
}

interface Cycle {
  label: string
  valeur: number
  desc: string
}

interface Profile {
  prenom: string
  nom: string
  date: string
  chemin_de_vie: Interpretation
  expression: Interpretation
  motivation: Interpretation
  realisation: Interpretation
  cycles: Cycle[]
  equilibre: string
  lettres_manquantes: string[]
  master_number: boolean
}

interface Props {
  profile: Profile
  onReset: () => void
}

export default function ProfileResult({ profile, onReset }: Props) {
  const p = profile

  return (
    <div className="space-y-6 animate-[fadeIn_0.4s_ease]">
      {/* Header */}
      <div className="text-center space-y-1 pb-2 border-b border-mystic-border">
        <p className="text-xs text-mystic-muted uppercase tracking-widest">Profil numérologique</p>
        <h2 className="font-serif text-2xl font-bold gradient-text">{p.prenom} {p.nom}</h2>
        <p className="text-xs text-mystic-muted">Né(e) le {p.date}</p>
        {p.master_number && (
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-mystic-gold/10 border border-mystic-gold/30 text-mystic-gold text-xs mt-1">
            <Star size={11} />
            Nombre maître — énergie spirituelle élevée
          </div>
        )}
      </div>

      {/* Core numbers */}
      <div className="space-y-3">
        <NumberCard
          number={p.chemin_de_vie.valeur}
          title="Chemin de vie"
          subtitle={p.chemin_de_vie.title}
          description={p.chemin_de_vie.text}
          icon="🌠"
          master={p.master_number}
        />
        <NumberCard
          number={p.expression.valeur}
          title="Nombre d'expression"
          subtitle={p.expression.title}
          description={p.expression.text}
          icon="🎭"
        />
        <NumberCard
          number={p.motivation.valeur}
          title="Nombre de motivation"
          subtitle={p.motivation.title}
          description={p.motivation.text}
          icon="💖"
        />
        <NumberCard
          number={p.realisation.valeur}
          title="Nombre de réalisation"
          subtitle={p.realisation.title}
          description={p.realisation.text}
          icon="🧱"
        />
      </div>

      {/* Cycles */}
      <div className="rounded-xl border border-mystic-border bg-mystic-card p-5 space-y-3">
        <p className="text-xs text-mystic-muted uppercase tracking-widest">🌀 Cycles de vie</p>
        <div className="space-y-2">
          {p.cycles.map((c, i) => (
            <div key={i} className="flex items-start gap-3">
              <span className="shrink-0 w-7 h-7 rounded-full bg-mystic-purple/20 border border-mystic-purple/30 flex items-center justify-center text-sm font-bold text-mystic-purple">
                {c.valeur}
              </span>
              <div>
                <p className="text-xs font-semibold text-mystic-text">{c.label}</p>
                <p className="text-xs text-mystic-muted">{c.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Balance */}
      <div className="rounded-xl border border-mystic-border bg-mystic-card px-5 py-4">
        <p className="text-xs text-mystic-muted uppercase tracking-widest mb-2">⚖️ Équilibre énergétique</p>
        <p className="text-sm text-mystic-text leading-relaxed">{p.equilibre}</p>
      </div>

      {/* Missing letters */}
      <div className="rounded-xl border border-mystic-border bg-mystic-card px-5 py-4">
        <p className="text-xs text-mystic-muted uppercase tracking-widest mb-2">💀 Lettres karmiques manquantes</p>
        {p.lettres_manquantes.length > 0 ? (
          <div className="flex flex-wrap gap-1.5 mt-1">
            {p.lettres_manquantes.map(l => (
              <span key={l} className="px-2 py-0.5 rounded bg-mystic-rose/10 border border-mystic-rose/20 text-mystic-rose text-xs font-mono font-bold">
                {l}
              </span>
            ))}
            <p className="w-full text-xs text-mystic-muted mt-1">Ces vibrations représentent des leçons karmiques à intégrer.</p>
          </div>
        ) : (
          <p className="text-sm text-mystic-teal">✨ Aucune — vous possédez toutes les vibrations alphabétiques.</p>
        )}
      </div>

      {/* Reset */}
      <button
        onClick={onReset}
        className="w-full py-2.5 rounded-lg border border-mystic-border text-mystic-muted hover:text-mystic-text hover:border-mystic-purple/40 transition-colors text-sm flex items-center justify-center gap-2"
      >
        <RotateCcw size={14} /> Nouvelle analyse
      </button>
    </div>
  )
}
