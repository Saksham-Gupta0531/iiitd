import { useState } from 'react'
import reactLogo from './assets/react.svg'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import { Home } from './Components/Home'
import { Form } from './Components/Form';

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={< Form/>} />
      </Routes>
    </Router>
  )
}

export default App
