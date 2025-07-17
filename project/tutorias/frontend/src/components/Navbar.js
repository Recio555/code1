import { Menu } from 'lucide-react';
import LanguageSelector from './LanguageSelector';

export default function Header({ t, language, setLanguage, mobileMenuOpen, setMobileMenuOpen }) {
  return (
    <header className="bg-blue-600 text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-xl font-bold">{t.title}</h1>

        {/* Desktop Language Selector */}
        <div className="hidden md:flex space-x-4">
          <LanguageSelector language={language} setLanguage={setLanguage} t={t} />
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label={t.toggleMenu}
        >
          <Menu />
        </button>
      </div>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className="mt-2 pt-2 border-t border-blue-500 md:hidden">
          <LanguageSelector language={language} setLanguage={setLanguage} t={t} />
        </div>
      )}
    </header>
  );
}




