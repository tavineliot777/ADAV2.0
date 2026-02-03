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

  useEffect(() => {
   
   axios.get('http://127.0.0.1:8000/api/osso/listar')
   .then((r) => {setOsso(r.data)})
   .catch(
    (erro) => {console.error("Nenhum osso encontrado!"), erro}
   ) 

  },[]);

  return(
    <div className='container'>

    <h1 style={{color: "black",padding: 10}}>{osso? osso.nome : "Nulo"}</h1>
    
    <div className = 'filho'>


      <Canvas dpr={[1,2]} camera={{fov: 45, position : [0,0,10] }}> 

        <color attach = 'background' args={['rgb(200,192,238)']}></color>
 
  <Suspense fallback={null}>
  
  <Stage environment="city" intensity={0.5}>
    {osso?.objeto3D && (
      <Modelo url={`http://127.0.0.1:8000${osso.objeto3D}`} />
    )}
  </Stage>
  
  </Suspense>

       <OrbitControls makeDefault />

      </Canvas>
    
    {osso ? (<ul> <li><p className='descricao'>{osso.descricao}</p></li></ul>) : null}

     </div>
    </div>
  )

}

export default App
