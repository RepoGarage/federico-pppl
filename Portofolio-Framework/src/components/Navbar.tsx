import Hamburger from "./Hamburger";
import { useLocation, Link } from "react-router-dom";

export default function Navbar() {
  const location = useLocation();
  const isHomePage = location.pathname === "/home";
  const isAboutPage = location.pathname === "/about";

  return (
    <header className="flex justify-between items-center bg-gray-800 text-white p-4">
      <h1 className="text-2xl font-bold ml-5 hover:text-blue-500 transition-colors">
        <a href="/home">Portofolio</a>
      </h1>
      <div className="block sm:hidden text-2xl">
        <Hamburger />
      </div>
      <ul className="hidden sm:flex space-x-6 mr-5 text-xl">
        <li>
          <Link
            to="/home"
            className={`transition-colors duration-200 ${
              isHomePage
                ? "text-blue-400 font-semibold border-b-2 border-blue-400 pb-1"
                : "text-white hover:text-blue-500"
            }`}
          >
            Home
          </Link>
        </li>
        <li>
          <Link
            to="/about"
            className={`transition-colors duration-200 ${
              isAboutPage
                ? "text-blue-400 font-semibold border-b-2 border-blue-400 pb-1"
                : "text-white hover:text-blue-500"
            }`}
          >
            About
          </Link>
        </li>
      </ul>
    </header>
  );
}
