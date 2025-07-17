import { Calendar, Star } from 'lucide-react';

export default function TutorCard({ tutor, t }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      <div className="flex items-center mb-4">
        <img src={tutor.image} alt={tutor.name} className="w-16 h-16 rounded-full mr-4 object-cover" />
        <div>
          <h3 className="font-semibold">{tutor.name}</h3>
          <div className="flex items-center text-yellow-500">
            <Star className="w-4 h-4 fill-current" />
            <span className="ml-1">{tutor.rating}</span>
          </div>
        </div>
      </div>
      <div className="mb-3">
        <div className="flex items-center text-sm text-gray-600 mb-1">
          <Calendar className="w-4 h-4 mr-1" />
          <span>{t.availability}: {tutor.availability}</span>
        </div>
        <div className="flex flex-wrap gap-1 mb-1">
          {tutor.subjects.map(subject => (
            <span key={subject} className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">
              {t[subject]}
            </span>
          ))}
        </div>
        <div className="flex flex-wrap gap-1">
          {tutor.languages.map(lang => (
            <span key={lang} className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded">
              {t[lang]}
            </span>
          ))}
        </div>
      </div>
      <div className="flex space-x-2">
        <button className="bg-gray-200 text-gray-800 py-1 px-3 rounded text-sm hover:bg-gray-300 flex-1">
          {t.viewProfile}
        </button>
        <button className="bg-blue-600 text-white py-1 px-3 rounded text-sm hover:bg-blue-700 flex-1">
          {t.bookSession}
        </button>
      </div>
    </div>
  );
}
