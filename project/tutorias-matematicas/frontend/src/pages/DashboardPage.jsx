import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import UpcomingSessions from '../components/Dashboard/UpcomingSessions';
import PastSessions from '../components/Dashboard/PastSessions';
import ProgressChart from '../components/Dashboard/ProgressChart';
import { useTranslation } from 'react-i18next';

const DashboardPage = () => {
  const { user } = useAuth();
  const { t } = useTranslation();
  const [activeTab, setActiveTab] = useState('upcoming');
  const [sessions, setSessions] = useState({
    upcoming: [],
    past: []
  });

  useEffect(() => {
    const fetchSessions = async () => {
      try {
        const response = await fetch(`/api/sessions/upcoming?user_id=${user.id}`);
        const data = await response.json();
        setSessions(prev => ({ ...prev, upcoming: data }));
      } catch (error) {
        console.error('Error fetching sessions:', error);
      }
    };
    
    fetchSessions();
  }, [user.id]);

  return (
    <div className="dashboard-container">
      <h1>{t('welcome')}, {user.full_name}</h1>
      
      <div className="dashboard-tabs">
        <button 
          className={activeTab === 'upcoming' ? 'active' : ''}
          onClick={() => setActiveTab('upcoming')}
        >
          {t('upcomingSessions')}
        </button>
        <button 
          className={activeTab === 'past' ? 'active' : ''}
          onClick={() => setActiveTab('past')}
        >
          {t('pastSessions')}
        </button>
        <button 
          className={activeTab === 'progress' ? 'active' : ''}
          onClick={() => setActiveTab('progress')}
        >
          {t('myProgress')}
        </button>
      </div>
      
      <div className="dashboard-content">
        {activeTab === 'upcoming' && <UpcomingSessions sessions={sessions.upcoming} />}
        {activeTab === 'past' && <PastSessions sessions={sessions.past} />}
        {activeTab === 'progress' && <ProgressChart />}
      </div>
    </div>
  );
};

export default DashboardPage;