import React, { useState } from 'react';
import { useSocket } from '../../hooks/useSocket';

const DocumentSharing = ({ documents, onUpload }) => {
  const [file, setFile] = useState(null);
  const [isUploading, setIsUploading] = useState(false);
  const socket = useSocket();

  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = () => {
    if (!file || !socket) return;

    setIsUploading(true);
    onUpload(file);

    setTimeout(() => {
      setIsUploading(false);
      socket.emit('document-uploaded', {
        name: file.name,
        type: file.type,
        size: file.size,
      });
      setFile(null);
    }, 1500);
  };

  const handleDownload = (doc) => {
    console.log('Downloading:', doc.name);
  };

  return (
    <div className="document-sharing">
      <div className="upload-section">
        <input type="file" onChange={handleFileChange} disabled={isUploading} />
        {file && (
          <div className="file-info">
            <span>{file.name}</span>
            <button onClick={handleUpload} disabled={isUploading || !socket}>
              {isUploading ? 'Subiendo...' : 'Subir'}
            </button>
          </div>
        )}
      </div>

      <div className="documents-list">
        <h3>Documentos Compartidos</h3>
        {documents.length === 0 ? (
          <p>No hay documentos compartidos aún</p>
        ) : (
          <ul>
            {documents.map((doc) => (
              <li key={doc.id} className="document-item">
                <div className="document-info">
                  <span className="document-name">{doc.name}</span>
                  <span className="document-meta">
                    {doc.type} - {Math.round(doc.size / 1024)} KB
                  </span>
                </div>
                <button onClick={() => handleDownload(doc)} className="download-btn">
                  Descargar
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default DocumentSharing;


