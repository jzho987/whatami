import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Outlet, Route, Routes } from 'react-router'
import { Home } from './screens'
import './index.css';
import NavBar from './components/nav_bar/NavBar';
import NavBarRow from './components/nav_bar/NavBarRow';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
          <div className='flex h-screen'>
            <NavBar>
              <NavBarRow path='home' text='Home' />
              <NavBarRow path='excersize' text='Excersize' />
            </NavBar>
            <Outlet />
          </div>
        }>
          <Route index path='home' element={<Home />}/>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
