export default function Footer() {
  return (
    <footer className="bg-gray-800 text-white py-4 mt-auto">
      <div className="container mx-auto text-center">
        <p className="text-sm hover hover:text-blue-500 transition-colors">
          &copy; {new Date().getFullYear()} Federico Matthew Pratama
        </p>
      </div>
    </footer>
  );
}
