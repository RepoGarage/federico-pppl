import Hamburger from "hamburger-react";
import { useState } from "react";
import { useLocation, Link } from "react-router-dom";

export default function HamburgerComponents() {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();
  const isHomePage = location.pathname === "/home" || location.pathname === "/";
  const isAboutPage = location.pathname === "/about";

  const handleLinkClick = () => {
    setIsOpen(false);
  };

  return (
    <div>
      <Hamburger toggled={isOpen} toggle={setIsOpen} />

      <div
        className={`fixed top-0 right-0 h-full w-64 bg-white dark:bg-slate-800 text-gray-800 dark:text-white transform transition-transform duration-300 z-50 ${
          isOpen ? "translate-x-0" : "translate-x-full"
        }`}
      >
        <header className="flex justify-end p-4">
          <Hamburger toggled={isOpen} toggle={setIsOpen} />
        </header>
        <nav className="mt-4 px-4">
          <ul>
            <li className="py-2">
              <Link
                to="/home"
                className={`${
                  isHomePage
                    ? "text-blue-400 font-semibold border-b-2 border-blue-400 pb-1"
                    : "text-gray-800 dark:text-white"
                }`}
                onClick={handleLinkClick}
              >
                Home
              </Link>
            </li>
            <li className="py-2">
              <Link
                to="/about"
                className={`${
                  isAboutPage
                    ? "text-blue-400 font-semibold border-b-2 border-blue-400 pb-1"
                    : "text-gray-800 dark:text-white"
                }`}
                onClick={handleLinkClick}
              >
                About
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}
