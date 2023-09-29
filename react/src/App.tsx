import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [counter, setCounter] = useState(0);
  const [randomUserJson, setRandomUserJson] = useState("");

  useEffect(() => {
    fetchRandomUserData().then((res) => setRandomUserJson(res));
  }, []);

  return (
    <div className="App">
      <h1>Button</h1>
      <p>{counter}</p>
      <button onClick={() => setCounter(counter + 1)}>+</button>
      <pre>{randomUserJson}</pre>
    </div>
  );
}

const fetchRandomUserData = async () => {
  const { data } = await axios.get(`https://randomuser.me/api`);
  return JSON.stringify(data);
};

export default App;
