import logo from './logo.svg';
import './App.css';

import BlogHomePage from './BlogCard';
import { isArrayEmpty } from './Utils';

// Podemos importar com qualquer nome.

function App() {

    // const blogArr = null; - isso irá gerar um erro.

    const blogArr = [
      {
        id: 1,
        title:'Blog Title 1',
        description: 'Lorem Ipsum'
      },
      {
        id: 2,
        title:'Blog Title 2',
        description: 'Lorem Ipsum'
      },
      {
        id: 3,
        title:'Blog Title 3',
        description: 'Lorem Ipsum'
      }
    ]
    
    const blogCards = isArrayEmpty(blogArr) ? [] : blogArr.map((item, pos) => {
      return (
        <BlogHomePage className={'Blog'} key={pos}  title={item.title} description={item.description} id={item.id}/>

        // <div className="BlogCard" key={item.id}>
        //  <h3>{item.title}</h3>
        //  <p>{item.description}</p>
        // </div>
      )
    })

    return (
      <div className="App">
        {blogCards}
      </div>
  );
}

export default App;