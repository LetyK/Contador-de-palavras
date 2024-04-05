import React, {useState} from 'React';
function App () {
   const [click, setClick] = useState (0)
   return (
    <div>
        <p> Você clicou {click} vezes</p>
        <button onClick={() => setClick(click+1)}>
            CLIQUE AQUI!
        </button>
    </div>
   );
}
   export default App;