import { useState } from 'react';
import { translations } from '../data/translations';
import { tutors as allTutors } from '../data/tutors';
import Header from '../components/common/Header';
import SubjectFilter from '../components/SubjectFilter';
import TutorList from '../components/TutorList';
import BottomNavigation from '../components/BottomNavigation';

export default function HomePage() {
  const [language, setLanguage] = useState('es');
  const [selectedSubject, setSelectedSubject] = useState('algebra');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const t = translations[language];
  const filteredTutors = allTutors.filter(tutor => tutor.subjects.includes(selectedSubject));

  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      <Header {...{ t, language, setLanguage, mobileMenuOpen, setMobileMenuOpen }} />
      <main className="flex-grow container mx-auto p-4">
        <SubjectFilter {...{ t, selectedSubject, setSelectedSubject }} />
        <TutorList tutors={filteredTutors} t={t} />
      </main>
      <BottomNavigation t={t} />
    </div>
  );
}
