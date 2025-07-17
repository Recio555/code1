import React, { createContext, useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

export const LanguageContext = createContext();

export const LanguageProvider = ({ children }) => {
  const { i18n } = useTranslation();
  const [currentLanguage, setCurrentLanguage] = useState(() => {
    return localStorage.getItem('language') || 'es';
  });

  useEffect(() => {
    // Cambiar el idioma cuando cambie currentLanguage
    i18n.changeLanguage(currentLanguage);
    localStorage.setItem('language', currentLanguage);
  }, [currentLanguage, i18n]);

  const changeLanguage = (language) => {
    setCurrentLanguage(language);
  };

  // Lista de idiomas disponibles
  const availableLanguages = [
    { code: 'es', name: 'Español' },
    { code: 'en', name: 'English' }
  ];

  const value = {
    currentLanguage,
    changeLanguage,
    availableLanguages
  };

  return (
    <LanguageContext.Provider value={value}>
      {children}
    </LanguageContext.Provider>
  );
};