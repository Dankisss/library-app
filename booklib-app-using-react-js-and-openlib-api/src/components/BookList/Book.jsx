import React from 'react';
import { Link } from 'react-router-dom';
import "./BookList.css";

const Book = (prop) => {
  console.log(prop)

  return (
    <div className='book-item flex flex-column flex-sb'>
      <div className='book-item-img'>
        <img src = {prop.book.covers} alt = "cover" />
      </div>
      <div className='book-item-info text-center'>
        <Link to = {`/book/${prop.book.id}`}>
          <div className='book-item-info-item title fw-7 fs-18'>
            <span>{prop.book.title}</span>
          </div>
        </Link>

        <div className='book-item-info-item author fs-15'>
          <span className='text-capitalize fw-7'>Author: </span>
          <span>{prop.book.author}</span>
        </div>

        <div className='book-item-info-item edition-count fs-15'>
          <span className='text-capitalize fw-7'>Total Editions: </span>
          <span>{prop.book.edition_count}</span>
        </div>

        <div className='book-item-info-item publish-year fs-15'>
          <span className='text-capitalize fw-7'>First Publish Year: </span>
          <span>{prop.book.first_publish_year}</span>
        </div>
      </div>
    </div>
  )
}

export default Book