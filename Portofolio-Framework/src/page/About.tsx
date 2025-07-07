export default function About() {
  return (
    <div className="font-poppins flex flex-col items-center text-center px-4">
      <div className="relative p-6 bg-white rounded-xl shadow-md">
        <h1 className="text-2xl md:text-3xl font-bold mb-4">About Me 🙋‍♂️</h1>{" "}
        <p className="text-lg text-gray-800 max-w-2xl text-justify mb-4">
          Hello! I'm Federico Matthew Pratama, a web developer with a strong
          interest in crafting responsive, user-friendly websites and
          applications. My journey in tech started with curiosity and has grown
          into a passion for clean code and modern UI/UX design.
        </p>
        <p className="text-lg text-gray-800 max-w-2xl text-justify mb-4">
          I specialize in frontend technologies like React, Tailwind CSS, and
          TypeScript, and I also enjoy working on backend logic with Go. I'm
          always open to learning new stacks and collaborating with others to
          solve real-world problems through code.
        </p>
        <p className="text-lg text-gray-800 max-w-xl text-justify">
          Outside of coding, I enjoy gaming, listening to music, and chilling at
          home. Nice to meet you!
        </p>
      </div>
      <div className="p-4">
        <div className="relative p-6 bg-white rounded-xl shadow-md">
          <p className="text-2xl font-semibold mb-4">Made with:</p>
          <div className="flex flex-col md:flex-row gap-3">
            <div className="bg-blue-500 text-white text-base font-medium rounded-lg px-4 py-2 shadow hover:bg-blue-600 transition">
              React
            </div>
            <div className="bg-indigo-500 text-white text-base font-medium rounded-lg px-4 py-2 shadow hover:bg-indigo-600 transition">
              TypeScript
            </div>
            <div className="bg-purple-500 text-white text-base font-medium rounded-lg px-4 py-2 shadow hover:bg-purple-600 transition">
              Vite
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
