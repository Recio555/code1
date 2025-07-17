import React from 'react';

export default function TutorSearch({ t }) {
  return (
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
          <option>{t.languageNames.es}</option>
          <option>{t.languageNames.en}</option>
          <option>{t.languageNames.fr}</option>
        </select>
        <button className="bg-blue-600 text-white p-2 rounded-lg flex items-center justify-center space-x-2">
          <span>{t.search}</span>
        </button>
      </div>
    </div>
  );
}
