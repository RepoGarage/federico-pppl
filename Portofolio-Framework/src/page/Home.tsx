import { TypeAnimation } from "react-type-animation";

export default function Home() {
  return (
    <div className="font-poppins flex flex-col lg:flex-row items-center justify-center gap-8">
      <img
        src="/halo.jpg"
        alt="Photo of Federico Matthew Pratama"
        className="w-79 rounded-2xl shadow-md"
      />
      <div className="flex flex-col text-left relative p-8 bg-white rounded-xl shadow-md">
        <div className="font-bold text-2xl md:text-3xl text-center md:text-left">
          <p>Hello There 👋</p>
          <TypeAnimation
            sequence={[
              "I'm Federico Matthew",
              2000,
              "I'm a Data Analyst",
              2000,
              "I'm a Web Developer",
              2000,
            ]}
            wrapper="span"
            speed={25}
            style={{ display: "inline-block" }}
            repeat={Infinity}
          />
        </div>
        <p className="text-lg mt-4 text-gray-800 max-w-md text-justify">
          I’m passionate about turning ideas into impactful digital experiences.
          Whether it’s analyzing data or building responsive web apps, I love
          solving real-world problems through tech.
        </p>
        <p className="text-2xl mt-10 text-center">Stay connect with me</p>
        <div className="flex justify-center">
          <div className="flex flex-col md:flex-row gap-4 mt-9">
            <a
              href="https://github.com/MashuNakamura"
              className="flex gap-3 bg-gray-700 text-white text-base font-medium rounded-lg px-4 py-3 shadow hover:bg-gray-800 transition"
            >
              <img src="github.png" alt="GitHub" className="w-6 h-6" />
              Github
            </a>
            <a
              href="https://www.instagram.com/federico.matthew01/"
              className="flex gap-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white text-base font-medium rounded-lg px-4 py-3 shadow hover:from-purple-600 hover:to-pink-600 transition"
            >
              <img src="instagram.png" alt="Instagram" className="w-6 h-6" />
              Instagram
            </a>
            <a
              href="https://discord.com/users/mashu23"
              className="flex gap-3 bg-indigo-600 text-white text-base font-medium rounded-lg px-4 py-3 shadow hover:bg-indigo-700 transition"
            >
              <img src="discord.png" alt="Discord" className="w-6 h-6" />
              Discord
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
