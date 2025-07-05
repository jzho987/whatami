import { useNavigate } from "react-router"

type NavBarRowProps = {
  text: string | undefined,
  path: string,
}


export default function NavBarRow({
  text,
  path,
}: NavBarRowProps) {

  const navigate = useNavigate();

  return (
    <button onClick={() => {
      navigate(path);
    }}>
      {text}
    </button>
  )
}
