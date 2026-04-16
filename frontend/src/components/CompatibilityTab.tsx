import { useState } from 'react'
import axios from 'axios'
import { AlertCircle, Heart, HeartCrack } from 'lucide-react'
import PersonForm, { PersonData } from './PersonForm'

interface CompatResult {
  personne1: { prenom: string; nom: string; chemin_de_vie: { valeur: number; title: string } }
  personne2: { prenom: string; nom: string; chemin_de_vie: { valeur: number; title: string } }
  compatibilite: { score: number; label: string; description: string }
}

export default function CompatibilityTab() {
  const [step, setStep] = useState<1 | 2>(1)
  const [person1, setPerson1] = useState<PersonData | null>(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<CompatResult | null>(null)
  const [error, setError] = useState('')

  const handlePerson1 = (data: PersonData) => {
    setPerson1(data)
    setStep(2)
  }

  const handlePerson2 = async (data: PersonData) => {
    if (!person1) return
    setLoading(true)
    setError('')
    try {
      const { data: res } = await axios.post('/api/compatibility', {
        personne1: person1,
        personne2: data,
      })
      setResult(res)
    } catch (e: unknown) {
      if (axios.isAxiosError(e)) {
        const detail = e.response?.data?.detail
        if (detail) setError(String(detail))
        else if (!e.response) setError('Serveur inaccessible — vérifiez que le backend tourne sur le port 8000.')
        else setError(`Erreur serveur ${e.response.status}`)
      } else {
        setError('Erreur inattendue.')
      }
    } finally {
      setLoading(false)
    }
  }

  const reset = () => {
    setStep(1)
    setPerson1(null)
    setResult(null)
    setError('')
  }

  const scoreColor = (s: number) =>
    s >= 80 ? 'text-emerald-400' : s >= 60 ? 'text-mystic-gold' : s >= 40 ? 'text-orange-400' : 'text-red-400'

  const scoreBar = (s: number) =>
    s >= 80 ? 'bg-emerald-400' : s >= 60 ? 'bg-mystic-gold' : s >= 40 ? 'bg-orange-400' : 'bg-red-400'

  if (result) {
    const { personne1, personne2, compatibilite: c } = result
    return (
      <div className="space-y-6 animate-[fadeIn_0.4s_ease]">
        {/* Versus card */}
        <div className="rounded-xl border border-mystic-border bg-mystic-card p-5">
          <div className="flex items-center justify-between gap-3">
            <div className="text-center flex-1">
              <p className="font-serif font-bold text-mystic-gold text-lg">{personne1.prenom}</p>
              <p className="text-xs text-mystic-muted">{personne1.nom}</p>
              <div className="mt-2 inline-block px-3 py-1 rounded-full bg-mystic-gold/10 border border-mystic-gold/30">
                <span className="text-mystic-gold font-bold font-serif text-xl">{personne1.chemin_de_vie.valeur}</span>
              </div>
              <p className="text-xs text-mystic-muted mt-1">{personne1.chemin_de_vie.title}</p>
            </div>

            <div className="flex flex-col items-center gap-1">
              {c.score >= 60
                ? <Heart size={28} className="text-mystic-rose animate-pulse" />
                : <HeartCrack size={28} className="text-red-400" />
              }
              <span className="text-xs text-mystic-muted">VS</span>
            </div>

            <div className="text-center flex-1">
              <p className="font-serif font-bold text-mystic-purple text-lg">{personne2.prenom}</p>
              <p className="text-xs text-mystic-muted">{personne2.nom}</p>
              <div className="mt-2 inline-block px-3 py-1 rounded-full bg-mystic-purple/10 border border-mystic-purple/30">
                <span className="text-mystic-purple font-bold font-serif text-xl">{personne2.chemin_de_vie.valeur}</span>
              </div>
              <p className="text-xs text-mystic-muted mt-1">{personne2.chemin_de_vie.title}</p>
            </div>
          </div>
        </div>

        {/* Score */}
        <div className="rounded-xl border border-mystic-border bg-mystic-card p-5 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs text-mystic-muted uppercase tracking-widest">Compatibilité</p>
              <p className={`text-xl font-bold font-serif mt-0.5 ${scoreColor(c.score)}`}>{c.label}</p>
            </div>
            <span className={`text-3xl font-bold font-serif ${scoreColor(c.score)}`}>{c.score}%</span>
          </div>
          <div className="h-2 rounded-full bg-mystic-border overflow-hidden">
            <div
              className={`h-full rounded-full transition-all duration-700 ${scoreBar(c.score)}`}
              style={{ width: `${c.score}%` }}
            />
          </div>
          <p className="text-sm text-mystic-muted">{c.description}</p>
        </div>

        <button
          onClick={reset}
          className="w-full py-2.5 rounded-lg border border-mystic-border text-mystic-muted hover:text-mystic-text hover:border-mystic-purple/40 transition-colors text-sm"
        >
          ↺ Nouvelle comparaison
        </button>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* Step indicator */}
      <div className="flex items-center gap-3">
        {[1, 2].map(s => (
          <div key={s} className={`flex-1 h-1 rounded-full transition-all ${s <= step ? 'bg-mystic-purple' : 'bg-mystic-border'}`} />
        ))}
      </div>

      {step === 1 && (
        <div className="space-y-4">
          <div className="text-center">
            <p className="text-xs text-mystic-muted uppercase tracking-widest">Étape 1 / 2</p>
            <p className="text-sm text-mystic-text/70 mt-1">Première personne</p>
          </div>
          <PersonForm onSubmit={handlePerson1} loading={false} label="Continuer →" color="gold" />
        </div>
      )}

      {step === 2 && (
        <div className="space-y-4">
          <div className="text-center space-y-1">
            <p className="text-xs text-mystic-muted uppercase tracking-widest">Étape 2 / 2</p>
            <p className="text-sm text-mystic-text/70">
              ✅ <span className="text-mystic-gold">{person1?.prenom} {person1?.nom}</span> enregistré(e)
            </p>
            <p className="text-xs text-mystic-muted">Maintenant la deuxième personne</p>
          </div>
          <PersonForm onSubmit={handlePerson2} loading={loading} label="Calculer la compatibilité ❤️" color="purple" />
          <button
            onClick={() => setStep(1)}
            className="w-full text-xs text-mystic-muted hover:text-mystic-text transition-colors"
          >
            ← Changer la première personne
          </button>
        </div>
      )}

      {error && (
        <div className="flex items-start gap-3 px-4 py-3 rounded-lg bg-red-950/30 border border-red-800/40">
          <AlertCircle size={16} className="text-red-400 mt-0.5 shrink-0" />
          <p className="text-sm text-red-400">{error}</p>
        </div>
      )}
    </div>
  )
}
