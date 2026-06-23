import { useState } from 'react'
import SearchForm from './SearchForm'
import BookCard from './BookCard'
import './App.css'

function App() {
  
  const [books, setBooks] = useState([])
  
  const [loading, setLoading] = useState(false)
  
  const [searched, setSearched] = useState(false)
  
  const [searchInput, setSearchInput] = useState('')
  
  const [error, setError] = useState(null)
  
  //APIをたたいて本を検索する関数
  const handleSearch = async (input) => {
    setLoading(true)
    setSearchInput(input)
    setError(null)
    try {
      
      const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/match?input=${encodeURIComponent(input)}`)
      if (!res.ok) throw new Error(`サーバーエラー (${res.status})`)
      const data = await res.json()
      setBooks(data)
      setSearched(true)
    } catch (e) {
      
      setError('検索に失敗しました。サーバーが起動しているか確認してください。')
      setBooks([])
    } finally {
      
      setLoading(false)
    }
  }

  //似た本を検索する関数
  const handleSimilar = (keywords) => {
    handleSearch(keywords.join(' '))
    window.scrollTo(0, 0)
  }

  return (
    <div className="container">
      <h1>思想で本を探そう</h1>
      
      <SearchForm onSearch={handleSearch} value={searchInput} onChange={setSearchInput} />
      
      {loading && <p className="loading">検索中...</p>}
      
      {!loading && error && <p className="error">{error}</p>}
      
      {!loading && !error && searched && books.length === 0 && (
        <p className="no-results">マッチする本が見つかりませんでした。別のキーワードで試してみてください。</p>
      )}
      
      <div className="book-list">
        {books.map((book, i) => (
          <BookCard key={i} book={book} onSimilar={handleSimilar} />
        ))}
      </div>
    </div>
  )
}

export default App
