import { useState } from 'react'
import axios from 'axios'
import { AlertCircle } from 'lucide-react'
import PersonForm, { PersonData } from './PersonForm'
import ProfileResult from './ProfileResult'

export default function ProfileTab() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<null | object>(null)
  const [error, setError] = useState('')

  const handleSubmit = async (data: PersonData) => {
    setLoading(true)
    setError('')
    setResult(null)
    try {
      const { data: res } = await axios.post('/api/analyze', data)
      setResult(res)
    } catch (e: unknown) {
      if (axios.isAxiosError(e)) {
        const detail = e.response?.data?.detail
        if (detail) setError(String(detail))
        else if (!e.response) setError('Impossible de contacter le serveur — vérifiez que le backend tourne sur le port 8000.')
        else setError(`Erreur serveur ${e.response.status}`)
      } else {
        setError('Erreur inattendue.')
      }
    } finally {
      setLoading(false)
    }
  }

  if (result) {
    return <ProfileResult profile={result as never} onReset={() => setResult(null)} />
  }

  return (
    <div className="space-y-6">
      <div className="text-center space-y-1">
        <p className="text-xs text-mystic-muted uppercase tracking-widest">Entrez vos informations</p>
        <p className="text-sm text-mystic-text/70">Votre prénom, nom complet et date de naissance suffisent pour révéler vos nombres.</p>
      </div>

      <PersonForm onSubmit={handleSubmit} loading={loading} />

      {error && (
        <div className="flex items-start gap-3 px-4 py-3 rounded-lg bg-red-950/30 border border-red-800/40">
          <AlertCircle size={16} className="text-red-400 mt-0.5 shrink-0" />
          <p className="text-sm text-red-400">{error}</p>
        </div>
      )}
    </div>
  )
}
