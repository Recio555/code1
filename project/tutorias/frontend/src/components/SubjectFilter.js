import { Search } from 'lucide-react';

export default function SubjectFilter({ t, selectedSubject, setSelectedSubject }) {
  return (
    <section className="bg-white rounded-lg shadow-md p-4 mb-6">
      <h2 className="text-lg font-semibold mb-4">{t.findTutor}</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">{t.subjects}</label>
          <select
            className="w-full p-2 border border-gray-300 rounded"
            value={selectedSubject}
            onChange={(e) => setSelectedSubject(e.target.value)}
          >
            <option value="algebra">{t.algebra}</option>
            <option value="calculus">{t.calculus}</option>
            <option value="geometry">{t.geometry}</option>
            <option value="statistics">{t.statistics}</option>
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">{t.language}</label>
          <select className="w-full p-2 border border-gray-300 rounded">
            <option value="any">---</option>
            <option value="es">{t.spanish}</option>
            <option value="en">{t.english}</option>
            <option value="fr">{t.french}</option>
          </select>
        </div>
        <div className="flex items-end">
          <button className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 flex items-center justify-center">
            <Search className="w-4 h-4 mr-2" />
            {t.search}
          </button>
        </div>
      </div>
    </section>
  );
}
