import './App.css';
import React, { useState,useEffect,Suspense } from 'react';
import axios from "axios";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, useGLTF, Stage, Center } from "@react-three/drei";


function Modelo({url}){

const {scene} = useGLTF(url);

return <primitive object={scene}/>

}



function App() {

  
  const [osso,setOsso] = useState(null);
  const [nomeDigitado,setNomeDigitado] = useState("");

  function enviarOsso(){

const dadosParaBuscar = {
  "nome" : nomeDigitado
 }

  axios.post('http://127.0.0.1:8000/api/osso/procurar_osso/', dadosParaBuscar)
  .then((e) => {setOsso(e.data)})
  .catch((erro) => console.error(erro));

}

  useEffect(() => {
    
    console.log("Busquei o osso inicial.");

    axios.get('http://127.0.0.1:8000/api/osso/listar') 
      .then((r) => {
        setOsso(r.data);       
        setNomeDigitado(r.data.nome || ""); 
      })
      .catch((erro) => console.error("Erro ao buscar inicial", erro));

  }, []);

  return(
    <div style={{display : 'flex', width : '100vw', height : '100vh'}}>
     <div style={{width : "30%",
      background : "#f0f0f0",
      padding : "20px",
      display : "flex",
      flexDirection : "column",
      gap : "10px"
     }}>

 <h1 style={{color: "black",padding: 10}}>{osso? osso.nome : "Nulo"}</h1>

{osso ? (<ul> <li><p className='descricao'>{osso.descricao}</p></li></ul>) : null}

       <input type="text" 
    placeholder='Procurar Osso'
     value={nomeDigitado}
     onChange={(e) => setNomeDigitado(e.target.value)}/>
    
    <button onClick={enviarOsso}>Procurar...</button>
   
     </div>
   
    
    <div style={{flex : 1, position : 'relative'}}>


      <Canvas dpr={[1,2]} camera={{fov: 45, position : [0,0,10] }}> 

        <color attach = 'background' args={['rgb(165, 164, 170)']}></color>
 
  <Suspense fallback={null}>
  
  <Stage environment="city" intensity={0.5}>
    {osso?.objeto3D && (
      <Modelo url={`http://127.0.0.1:8000${osso.objeto3D}`} />
    )}
  </Stage>
  
  </Suspense>

       <OrbitControls makeDefault />

      </Canvas>
 
   
     </div>
    </div>
  )

}

export default App
