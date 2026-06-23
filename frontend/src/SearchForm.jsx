import { useState } from 'react'

// 例文チップ
const EXAMPLES = [
  '自由とは何かを知りたい',
  '死や存在について考える',
  '愛について考えている',
]

//　検索窓の関数
function SearchForm({ onSearch, value, onChange }) {

  // 検索が実行されたときの関数
  const handleSubmit = (e) => {
    
    e.preventDefault()
    
    if (value.trim()) onSearch(value)
  }

  // 例文チップが実行された時の関数
  const handleExample = (text) => {
    
    onChange(text)
    onSearch(text)
  }

  return (
    <div className="search-wrapper">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="知りたいことや考えを入力してください"
        />
        {value && <button type="button" onClick={() => onChange('')}>×</button>}
        <button type="submit">検索</button>
      </form>
      
      <div className="examples">
        <span className="examples-label">例：</span>
        {EXAMPLES.map((text, i) => (
          <button
            key={i}
            type="button"
            className="example-chip"
            onClick={() => handleExample(text)}
          >
            {text}
          </button>
        ))}
      </div>
    </div>
  )
}

export default SearchForm
