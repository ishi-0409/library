import { useState } from 'react'

const GENRES = ['哲学', '文学', 'ビジネス', '心理学', '歴史', '社会学', '経済学', '政治', '宗教']
const API_URL = 'https://9lkbaom8zg.execute-api.ap-northeast-1.amazonaws.com'

function BookRequestModal({ isOpen, onClose }) {
  const [title, setTitle] = useState('')
  const [author, setAuthor] = useState('')
  const [genre, setGenre] = useState('哲学')
  const [reasonKeywords, setReasonKeywords] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [successMsg, setSuccessMsg] = useState('')

  if (!isOpen) return null

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!title.trim()) {
      setError('本のタイトルを入力してください。')
      return
    }

    setLoading(true)
    setError('')
    setSuccessMsg('')

    try {
      const res = await fetch(`${API_URL}/requests`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: title.trim(),
          author: author.trim(),
          genre: genre,
          reason_keywords: reasonKeywords.trim(),
        }),
      })

      if (!res.ok) {
        throw new Error('リクエストの送信に失敗しました。')
      }

      setSuccessMsg('✨ リクエストを送信しました！管理者が確認して登録します。')
      
      setTitle('')
      setAuthor('')
      setReasonKeywords('')
      
      setTimeout(() => {
        setSuccessMsg('')
        onClose()
      }, 2000)

    } catch (err) {
      setError(err.message || '通信エラーが発生しました。')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>📩 本の追加リクエスト</h2>
          <button className="modal-close-btn" onClick={onClose}>×</button>
        </div>

        <p className="modal-subtitle">
          追加してほしい本のタイトルや理由を教えてください。管理者が確認の上、ライブラリに追加登録します！
        </p>

        {error && <div className="modal-error">{error}</div>}
        {successMsg && <div className="modal-success">{successMsg}</div>}

        <form onSubmit={handleSubmit} className="modal-form">
          <div className="form-group">
            <label>追加してほしい本のタイトル <span className="required">*</span></label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="例: 方法序説"
              disabled={loading}
              required
            />
          </div>

          <div className="form-group">
            <label>著者名</label>
            <input
              type="text"
              value={author}
              onChange={(e) => setAuthor(e.target.value)}
              placeholder="例: デカルト"
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label>ジャンル</label>
            <select value={genre} onChange={(e) => setGenre(e.target.value)} disabled={loading}>
              {GENRES.map((g) => (
                <option key={g} value={g}>{g}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>関連キーワードや追加してほしい理由</label>
            <input
              type="text"
              value={reasonKeywords}
              onChange={(e) => setReasonKeywords(e.target.value)}
              placeholder="例: 自由, 思考のベースとなるおすすめの本"
              disabled={loading}
            />
          </div>

          <div className="modal-actions">
            <button type="button" className="btn-cancel" onClick={onClose} disabled={loading}>
              キャンセル
            </button>
            <button type="submit" className="btn-submit" disabled={loading}>
              {loading ? '送信中...' : 'リクエストを送信'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default BookRequestModal
