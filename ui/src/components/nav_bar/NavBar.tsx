import { useState } from "react";
import { IoMenu } from "react-icons/io5";

type NavBarProps = {
  children: React.ReactNode;
}


export default function NavBar({
  children
}: NavBarProps) {
  
  const [isOpen, setIsOpen] = useState(true)

  return (
    <div className='min-w-5 flex flex-col items-center transition-all duration-1000 gap-10 p-5 bg-slate-100 shadow-lg shadow-stone-500 overflow-y-auto'>
      <button onClick={() => {
        setIsOpen(!isOpen)
      }}>
        <IoMenu className='text-lg' />
      </button>
      {isOpen && children}
    </div>
  )
}
