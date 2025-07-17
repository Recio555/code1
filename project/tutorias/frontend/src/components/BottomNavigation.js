import { Search, Calendar, MessageSquare, BookOpen } from 'lucide-react';

export default function BottomNavigation({ t }) {
  return (
    <nav className="bg-white border-t border-gray-200 fixed bottom-0 inset-x-0 z-10">
      <div className="flex justify-around">
        <a href="#" className="flex flex-col items-center py-2 px-4 text-blue-600">
          <Search className="w-6 h-6" />
          <span className="text-xs">{t.findTutor}</span>
        </a>
        <a href="#" className="flex flex-col items-center py-2 px-4 text-gray-500">
          <Calendar className="w-6 h-6" />
          <span className="text-xs">{t.upcomingSessions}</span>
        </a>
        <a href="#" className="flex flex-col items-center py-2 px-4 text-gray-500">
          <MessageSquare className="w-6 h-6" />
          <span className="text-xs">Chat</span>
        </a>
        <a href="#" className="flex flex-col items-center py-2 px-4 text-gray-500">
          <BookOpen className="w-6 h-6" />
          <span className="text-xs">{t.resources}</span>
        </a>
      </div>
    </nav>
  );
}
