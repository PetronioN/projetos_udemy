import logo from './logo.svg';
import './App.css';

function App() {
  const firstName = 'Full';
  const lastName = 'Name';
  const age = 28;
  const job = 'job';

  const mArr = [1, 2, 3, 4];

  const mObj = {
    name: 'name',
    age: 18
  }

  const inputPlaceholder = 'Enter Your Details'

  const getFullName = (firstName, lastName) => {
    return `${firstName} ${lastName}`
  }

  const detailsInputBox = <input placeholder={inputPlaceholder}
  autoComplete />;


  const styles = {
    margin: '16px',
    padding: '16px',
    boxSizing: 'border-box',
    borderRadius: '5px',
    boxShadow: '0 2px 5px #ccc'
  }

  return (
    <div className="App">
      <h3 style={styles}>Nome Completo: {firstName} {lastName}</h3>
      <h3 style={styles}>Nome Completo: {firstName + ' ' + lastName}</h3>
      <h3 style={styles}>Nome Completo: {`${firstName} ${lastName}`}</h3>
      <h3 style={styles}>Nome completo: {getFullName(firstName, lastName)}</h3>
      <p style={styles}>Idade: {age}</p>
      <p style={styles}>Trabalho: {job}</p>
      <p style={styles}>Idade: {mObj.age}</p>

      <input placeholder ={inputPlaceholder} autoComplete/>

      {detailsInputBox}
      <br />

      {mArr[0]}

      
    </div>
  );
}

export default App;
