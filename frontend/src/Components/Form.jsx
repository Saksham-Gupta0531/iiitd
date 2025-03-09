import React, { useState } from 'react';
import axios from 'axios';
import './Form.css';

export const Form = () => {
    const [activeTab, setActiveTab] = useState(true);
    const [selectedDB, setSelectedDB] = useState("Global");
    const [query, setQuery] = useState("");
    const [aiQuery, setAiQuery] = useState("");
    const [queryResult, setQueryResult] = useState([]);
    const [columns, setColumns] = useState([]);

    const handleQueryExecution = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/execute-query/', {
                db: selectedDB,
                query: activeTab ? query : aiQuery
            });
            console.log("Response:", response.data);
            if (response.data.data && response.data.data.length > 0) {
                setQueryResult(response.data.data);

                // Extract column names dynamically
                setColumns(Object.keys(response.data.data[0]));
            } else {
                setQueryResult([]);
                setColumns([]);
            }
        } catch (error) {
            console.error("Error executing query:", error);
            alert("Failed to execute query.");
        }
    };

    return (
        <div className='form-main'>
            <div className="title">
                <span className='title1'>Query </span>
                <span className='title2'>Execution </span>
                <span className='title1'>System</span>
            </div>
            <div className="main-content">
                <div className="left">
                    <div className="banner"></div>

                    <div className="btn1">
                        <button
                            className={`btn1-1 ${activeTab ? 'active' : ''}`}
                            onClick={() => setActiveTab(true)}
                        >
                            Custom Based
                        </button>
                        <button
                            className={`btn1-2 ${!activeTab ? 'active' : ''}`}
                            onClick={() => setActiveTab(false)}
                        >
                            AI Based
                        </button>
                    </div>

                    <div className="form">
                        {!activeTab ? (
                            <div className="ai-based">
                                <label>AI Based Query Execution</label>
                                <select
                                    className='opt'
                                    value={selectedDB}
                                    onChange={(e) => setSelectedDB(e.target.value)}
                                >
                                    <option value="Global">Global</option>
                                    <option value="MYSQL">MYSQL</option>
                                    <option value="PostgreSQL">PostgreSQL</option>
                                    <option value="SQLite3">SQLite3</option>
                                </select>
                                <textarea
                                    className="query-input"
                                    rows="5"
                                    placeholder="AI-generated query will appear here..."
                                    value={aiQuery}
                                    onChange={(e) => setAiQuery(e.target.value)}
                                ></textarea> <br />
                                <button className="run-query" onClick={handleQueryExecution}>Run AI Query</button>
                            </div>
                        ) : (
                            <div className="custom-based">
                                <label>Select DataBase Management System</label>
                                <select
                                    className='opt'
                                    value={selectedDB}
                                    onChange={(e) => setSelectedDB(e.target.value)}
                                >
                                    <option value="Global">Global</option>
                                    <option value="MYSQL">MYSQL</option>
                                    <option value="PostgreSQL">PostgreSQL</option>
                                    <option value="SQLite3">SQLite3</option>
                                </select>

                                <div className='form-head'>Enter Query</div>
                                <textarea
                                    className="query-input"
                                    rows="5"
                                    placeholder="Write your SQL query here..."
                                    value={query}
                                    onChange={(e) => setQuery(e.target.value)}
                                ></textarea><br />
                                <button className="run-query" onClick={handleQueryExecution}>Run Query</button>
                            </div>
                        )}
                    </div>
                </div>
                <div className="right">
                    <h3>Query Results</h3>
                    {queryResult.length > 0 ? (
                        <table className="query-result-table">
                            <thead>
                                <tr>
                                    {columns.map((col, index) => (
                                        <th key={index}>{col}</th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {queryResult.map((row, rowIndex) => (
                                    <tr key={rowIndex}>
                                        {columns.map((col, colIndex) => (
                                            <td key={colIndex}>{row[col]}</td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    ) : (
                        <p>No results to display.</p>
                    )}
                </div>
            </div>
        </div>
    );
};
