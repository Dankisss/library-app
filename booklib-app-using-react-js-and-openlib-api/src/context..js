import React, { useState, useContext, useEffect } from 'react';
import { useCallback } from 'react';
const URL = "http://localhost:8000/api/book/search/";
const AppContext = React.createContext();

const AppProvider = ({ children }) => {
    const [searchTerm, setSearchTerm] = useState("");
    const [books, setBooks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [resultTitle, setResultTitle] = useState("");

    const fetchBooks = useCallback(async () => {
        setLoading(true);
        try {
            const query = searchTerm ? `?q=${searchTerm}` : "";

            const response = await fetch(`${URL}${query}`);
            
            const data = await response.json();

            console.log(data);
            
            if (data) {
                // const newBooks = data.slice(0, 20).map((bookSingle) => {
                //     const { key, author_name, cover_i, edition_count, first_publish_year, title } = bookSingle;

                //     return {
                //         id: key,
                //         author: author_name,
                //         cover_id: cover_i,
                //         edition_count: edition_count,
                //         first_publish_year: first_publish_year,
                //         title: title
                //     }
                // });
                
                console.log("New books: ", data);

                setBooks(data);

                if (data.length > 1) {
                    setResultTitle("Your Search Result");
                } else {
                    setResultTitle("No Search Result Found!")
                }
            } else {
                setBooks([]);
                setResultTitle("No Search Result Found!");
            }
            setLoading(false);
        } catch (error) {
            console.log(error);
            setLoading(false);
        }
    }, [searchTerm]);

    useEffect(() => {
        fetchBooks();
    }, [searchTerm, fetchBooks]);

    console.log("Books context:", books)
    return (
        <AppContext.Provider value={{
            loading, books, setSearchTerm, resultTitle, setResultTitle,
        }}>
            {children}
        </AppContext.Provider>
    )
}

export const useGlobalContext = () => {
    return useContext(AppContext);
}

export { AppContext, AppProvider };