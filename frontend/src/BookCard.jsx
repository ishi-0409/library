

// ほんのカードの描画の関数
function BookCard({ book, onSimilar }) {
  
  const maxScore = 5
  const score = book.score

  return (
    <div className="book-card">
      
      {/*本の表紙画像 */}
      {book.cover_image_url ? (
        <img src={book.cover_image_url} alt={book.title} className="cover-image" />
      ) : (
        <div className="cover-placeholder" />
      )}

      {/*本の情報 */}
      <div className="book-info">

        {/*本のバッジ */}
        <div className="book-header">
          {book.genre && (
            <span
              className="genre-badge"
              style={{ backgroundColor: book.genre_color || '#999' }}
            >
              {book.genre}
            </span>
          )}
          
          {/*マッチ度*/}
          <div className="score-dots">
            <span>マッチ度</span>
            {Array.from({ length: maxScore }, (_, i) => (
              <span key={i} className={`dot ${i < score ? 'filled' : ''}`} />
            ))}
          </div>
        </div>

        <h2>{book.title}</h2>
        <p className="author">{book.author}</p>

        {/* 著者メッセージ */}
        {book.author_message && (
          <p className="author-message">{book.author_message}</p>
        )}

        {/* キーワードタグ*/}
        <div className="keywords">
          {book.ideology_keywords.map((keyword, i) => (
            <span key={i} className="tag">{keyword}</span>
          ))}
        </div>

        {/* アクションボタン */}
        <div className="book-actions">
          {/*似ている本 */}
          <button
            type="button"
            className="similar-btn"
            onClick={() => onSimilar(book.ideology_keywords)}
          >
            似た本を見る
          </button>
          
          {/*試し読み */}
          {book.preview_url && (
            <a
              href={book.preview_url}
              target="_blank"
              rel="noopener noreferrer"
              className="preview-btn"
            >
              試し読み
            </a>
          )}
        </div>
      </div>
    </div>
  )
}

export default BookCard
