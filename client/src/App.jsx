import './App.css'
import UserModal from './components/UserModal'
import UserTable from './components/UserTable'
import { Toaster } from 'alert';


function App() {
  return (
    <main className={"w-screen h-screen p-5 flex flex-col items-center  gap-5"}>
      <h1 className={"italic text-2xl"}>Smile-2-Step</h1>
      <Toaster position="top-center" />
      <UserModal />
      <UserTable />
    </main>
  )
}

export default App
