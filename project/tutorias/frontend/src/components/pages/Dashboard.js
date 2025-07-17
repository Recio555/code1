import { useState } from 'react';
import { Book, Globe, User, Video, MessageSquare, CheckCircle, BarChart, Star, Search } from 'lucide-react';
//import '../css/MathTutorApp.css';


export default function MathTutorApp() {
  const [activeTab, setActiveTab] = useState('home');
  const [language, setLanguage] = useState('es');
  const [mathTopic, setMathTopic] = useState('algebra');

  
  const translations = {
    es: {
      appName: "MathTutor Global",
      home: "Inicio",
      tutors: "Tutores",
      courses: "Cursos",
      practice: "Práctica",
      findTutor: "Encuentra un tutor",
      startNow: "Comenzar ahora",
      welcomeMessage: "Tutorías de matemáticas en tu idioma",
      popularTopics: "Temas populares",
      algebra: "Álgebra",
      calculus: "Cálculo",
      geometry: "Geometría",
      statistics: "Estadística",
      selectLanguage: "Seleccionar idioma",
      selectTopic: "Seleccionar tema",
      search: "Buscar",
      upcomingSessions: "Próximas sesiones",
      noSessions: "No tienes sesiones programadas",
      bookSession: "Reservar sesión",
      progress: "Tu progreso",
      joinLive: "Unirse ahora",
      featuredTutors: "Tutores destacados"
    },
    en: {
      appName: "MathTutor Global",
      home: "Home",
      tutors: "Tutors",
      courses: "Courses",
      practice: "Practice",
      findTutor: "Find a tutor",
      startNow: "Start now",
      welcomeMessage: "Math tutoring in your language",
      popularTopics: "Popular topics",
      algebra: "Algebra",
      calculus: "Calculus",
      geometry: "Geometry",
      statistics: "Statistics",
      selectLanguage: "Select language",
      selectTopic: "Select topic",
      search: "Search",
      upcomingSessions: "Upcoming sessions",
      noSessions: "No scheduled sessions",
      bookSession: "Book session",
      progress: "Your progress",
      joinLive: "Join now",
      featuredTutors: "Featured tutors"
    },
    fr: {
      appName: "MathTutor Global",
      home: "Accueil",
      tutors: "Tuteurs",
      courses: "Cours",
      practice: "Pratique",
      findTutor: "Trouver un tuteur",
      startNow: "Commencer",
      welcomeMessage: "Tutorat de mathématiques dans votre langue",
      popularTopics: "Sujets populaires",
      algebra: "Algèbre",
      calculus: "Calcul",
      geometry: "Géométrie",
      statistics: "Statistiques",
      selectLanguage: "Sélectionner la langue",
      selectTopic: "Sélectionner un sujet",
      search: "Rechercher",
      upcomingSessions: "Sessions à venir",
      noSessions: "Pas de sessions programmées",
      bookSession: "Réserver une session",
      progress: "Votre progression",
      joinLive: "Rejoindre maintenant",
      featuredTutors: "Tuteurs en vedette"
    }
  };

  const t = translations[language];
  
  // Tutores de ejemplo
  const tutors = [
    { id: 1, name: "María González", rating: 4.9, speciality: t.algebra, languages: ["es", "en"], img: "/api/placeholder/60/60" },
    { id: 2, name: "John Smith", rating: 4.8, speciality: t.calculus, languages: ["en", "fr"], img: "/api/placeholder/60/60" },
    { id: 3, name: "Sophie Dubois", rating: 4.9, speciality: t.geometry, languages: ["fr", "en"], img: "/api/placeholder/60/60" }
  ];

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-blue-600 text-white p-4">
        <div className="flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Book size={24} />
            <h1 className="text-xl font-bold">{t.appName}</h1>
          </div>
          <div className="flex space-x-4">
            <select 
              className="bg-blue-700 text-white px-2 py-1 rounded" 
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
            >
              <option value="es">Español</option>
              <option value="en">English</option>
              <option value="fr">Français</option>
            </select>
            <button className="bg-white text-blue-600 px-3 py-1 rounded flex items-center space-x-1">
              <User size={16} />
              <span>Login</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto p-4">
        {activeTab === 'home' && (
          <div>
            {/* Hero Banner */}
            <div className="bg-blue-500 text-white p-6 rounded-lg mb-6">
              <div className="flex flex-col md:flex-row items-center justify-between">
                <div className="mb-4 md:mb-0">
                  <h2 className="text-2xl font-bold mb-2">{t.welcomeMessage}</h2>
                  <p className="mb-4">
                    {language === 'es' && "Conecta con tutores certificados en más de 20 idiomas"}
                    {language === 'en' && "Connect with certified tutors in over 20 languages"}
                    {language === 'fr' && "Connectez-vous avec des tuteurs certifiés dans plus de 20 langues"}
                  </p>
                  <button className="bg-white text-blue-600 px-4 py-2 rounded-lg font-medium">
                    {t.startNow}
                  </button>
                </div>
                <div className="bg-blue-400 p-3 rounded-lg">
                  <Globe size={100} />
                </div>
              </div>
            </div>

            {/* Topics */}
            <div className="mb-6">
              <h3 className="text-lg font-medium mb-3">{t.popularTopics}</h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                <button 
                  className={`p-4 rounded-lg flex flex-col items-center justify-center ${mathTopic === 'algebra' ? 'bg-blue-100 border-2 border-blue-500' : 'bg-white'}`}
                  onClick={() => setMathTopic('algebra')}
                >
                  <div className="text-blue-500 mb-2">Σ</div>
                  <span>{t.algebra}</span>
                </button>
                <button 
                  className={`p-4 rounded-lg flex flex-col items-center justify-center ${mathTopic === 'calculus' ? 'bg-blue-100 border-2 border-blue-500' : 'bg-white'}`}
                  onClick={() => setMathTopic('calculus')}
                >
                  <div className="text-blue-500 mb-2">∫</div>
                  <span>{t.calculus}</span>
                </button>
                <button 
                  className={`p-4 rounded-lg flex flex-col items-center justify-center ${mathTopic === 'geometry' ? 'bg-blue-100 border-2 border-blue-500' : 'bg-white'}`}
                  onClick={() => setMathTopic('geometry')}
                >
                  <div className="text-blue-500 mb-2">△</div>
                  <span>{t.geometry}</span>
                </button>
                <button 
                  className={`p-4 rounded-lg flex flex-col items-center justify-center ${mathTopic === 'statistics' ? 'bg-blue-100 border-2 border-blue-500' : 'bg-white'}`}
                  onClick={() => setMathTopic('statistics')}
                >
                  <div className="text-blue-500 mb-2">σ</div>
                  <span>{t.statistics}</span>
                </button>
              </div>
            </div>

            {/* Find Tutor Search */}
            <div className="bg-white p-4 rounded-lg mb-6">
              <h3 className="text-lg font-medium mb-3">{t.findTutor}</h3>
              <div className="flex flex-col md:flex-row space-y-3 md:space-y-0 md:space-x-3">
                <select className="border p-2 rounded-lg flex-1">
                  <option>{t.selectTopic}</option>
                  <option>{t.algebra}</option>
                  <option>{t.calculus}</option>
                  <option>{t.geometry}</option>
                  <option>{t.statistics}</option>
                </select>
                <select className="border p-2 rounded-lg flex-1">
                  <option>{t.selectLanguage}</option>
                  <option>Español</option>
                  <option>English</option>
                  <option>Français</option>
                  <option>Português</option>
                  <option>中文</option>
                </select>
                <button className="bg-blue-600 text-white p-2 rounded-lg flex items-center justify-center space-x-2">
                  <Search size={18} />
                  <span>{t.search}</span>
                </button>
              </div>
            </div>

            {/* Upcoming Sessions */}
            <div className="bg-white p-4 rounded-lg mb-6">
              <h3 className="text-lg font-medium mb-3">{t.upcomingSessions}</h3>
              <div className="border rounded-lg p-4 bg-gray-50 text-center mb-3">
                <p className="text-gray-500">{t.noSessions}</p>
                <button className="mt-2 text-blue-600 font-medium">
                  {t.bookSession} →
                </button>
              </div>
            </div>

            {/* Featured Tutors */}
            <div className="bg-white p-4 rounded-lg">
              <h3 className="text-lg font-medium mb-3">{t.featuredTutors}</h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {tutors.map(tutor => (
                  <div key={tutor.id} className="border rounded-lg p-3 flex items-center space-x-3">
                    <img src={tutor.img} className="rounded-full" alt={tutor.name} />
                    <div>
                      <h4 className="font-medium">{tutor.name}</h4>
                      <p className="text-sm text-gray-600">{tutor.speciality}</p>
                      <div className="flex items-center text-sm">
                        <Star size={14} className="text-yellow-500 fill-yellow-500" />
                        <span className="ml-1">{tutor.rating}</span>
                        <div className="ml-2 flex space-x-1">
                          {tutor.languages.map(lang => (
                            <span key={lang} className="bg-blue-100 text-blue-800 text-xs px-1 rounded">
                              {lang}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Bottom Navigation */}
      <nav className="bg-white border-t flex justify-around p-2">
        <button 
          className={`flex flex-col items-center p-2 rounded ${activeTab === 'home' ? 'text-blue-600' : 'text-gray-600'}`}
          onClick={() => setActiveTab('home')}
        >
          <Book size={20} />
          <span className="text-xs">{t.home}</span>
        </button>
        <button 
          className={`flex flex-col items-center p-2 rounded ${activeTab === 'tutors' ? 'text-blue-600' : 'text-gray-600'}`}
          onClick={() => setActiveTab('tutors')}
        >
          <User size={20} />
          <span className="text-xs">{t.tutors}</span>
        </button>
        <button 
          className={`flex flex-col items-center p-2 rounded ${activeTab === 'courses' ? 'text-blue-600' : 'text-gray-600'}`}
          onClick={() => setActiveTab('courses')}
        >
          <Video size={20} />
          <span className="text-xs">{t.courses}</span>
        </button>
        <button 
          className={`flex flex-col items-center p-2 rounded ${activeTab === 'practice' ? 'text-blue-600' : 'text-gray-600'}`}
          onClick={() => setActiveTab('practice')}
        >
          <CheckCircle size={20} />
          <span className="text-xs">{t.practice}</span>
        </button>
      </nav>
    </div>
  );
}


