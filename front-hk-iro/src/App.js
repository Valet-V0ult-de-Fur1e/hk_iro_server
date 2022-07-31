import Navbar from './components/Navbar/index';
import { BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import Home from './pages';
import Blogs from './pages/blogs';
import SignUp from './pages/signup';
import Form from './pages/form_maked'

function App() {
return (
    <Router>
    <Navbar />
    <Routes>
        <Route exact path='/' element={<Home />} />
        <Route path='/blogs' element={<Blogs/>} />
        <Route path='/sign-up' element={<SignUp/>} />
        <Route path='/form-ok' element={<Form/>} />
    </Routes>
    </Router>
);
}
  
export default App;