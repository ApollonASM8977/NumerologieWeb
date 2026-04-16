import { useState } from 'react'
import { Sparkles, Loader2 } from 'lucide-react'

export interface PersonData {
  prenom: string
  nom: string
  jour: number
  mois: number
  annee: number
}

interface Props {
  onSubmit: (data: PersonData) => void
  loading: boolean
  label?: string
  color?: 'gold' | 'purple'
}

export default function PersonForm({ onSubmit, loading, label = 'Calculer mon profil', color = 'gold' }: Props) {
  const [form, setForm] = useState({ prenom: '', nom: '', jour: '', mois: '', annee: '' })

  const set = (k: string) => (e: React.ChangeEvent<HTMLInputElement>) =>
    setForm(f => ({ ...f, [k]: e.target.value }))

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!form.prenom || !form.nom || !form.jour || !form.mois || !form.annee) return
    onSubmit({
      prenom: form.prenom.trim(),
      nom: form.nom.trim(),
      jour: parseInt(form.jour),
      mois: parseInt(form.mois),
      annee: parseInt(form.annee),
    })
  }

  const btnClass = color === 'gold'
    ? 'bg-mystic-gold text-mystic-bg hover:shadow-gold'
    : 'bg-mystic-purple text-white hover:shadow-purple'

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="grid grid-cols-2 gap-3">
        <div>
          <label className="block text-xs text-mystic-muted uppercase tracking-widest mb-1.5">Prénom</label>
          <input
            className="mystic-input w-full px-3 py-2.5 rounded-lg text-sm"
            placeholder="Marie"
            value={form.prenom}
            onChange={set('prenom')}
            required
          />
        </div>
        <div>
          <label className="block text-xs text-mystic-muted uppercase tracking-widest mb-1.5">Nom</label>
          <input
            className="mystic-input w-full px-3 py-2.5 rounded-lg text-sm"
            placeholder="Dupont"
            value={form.nom}
            onChange={set('nom')}
            required
          />
        </div>
      </div>

      <div>
        <label className="block text-xs text-mystic-muted uppercase tracking-widest mb-1.5">Date de naissance</label>
        <div className="grid grid-cols-3 gap-3">
          <input
            className="mystic-input w-full px-3 py-2.5 rounded-lg text-sm text-center"
            placeholder="JJ"
            type="number" min="1" max="31"
            value={form.jour}
            onChange={set('jour')}
            required
          />
          <input
            className="mystic-input w-full px-3 py-2.5 rounded-lg text-sm text-center"
            placeholder="MM"
            type="number" min="1" max="12"
            value={form.mois}
            onChange={set('mois')}
            required
          />
          <input
            className="mystic-input w-full px-3 py-2.5 rounded-lg text-sm text-center"
            placeholder="AAAA"
            type="number" min="1900" max="2025"
            value={form.annee}
            onChange={set('annee')}
            required
          />
        </div>
      </div>

      <button
        type="submit"
        disabled={loading}
        className={`w-full py-3 rounded-lg font-semibold text-sm tracking-wider uppercase transition-all ${btnClass} disabled:opacity-40 disabled:cursor-not-allowed`}
      >
        {loading ? (
          <span className="flex items-center justify-center gap-2">
            <Loader2 size={16} className="animate-spin" /> Calcul en cours...
          </span>
        ) : (
          <span className="flex items-center justify-center gap-2">
            <Sparkles size={16} /> {label}
          </span>
        )}
      </button>
    </form>
  )
}
