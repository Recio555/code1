import React, { useState } from 'react';
import { uploadFile } from '../../../api/files';
import { useSession } from '../../../contexts/SessionContext';

const FileUpload = ({ roomId }) => {
  const [file, setFile] = useState(null);
  const [isUploading, setIsUploading] = useState(false);
  const [progress, setProgress] = useState(0);
  const { currentUser } = useSession();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    
    setIsUploading(true);
    try {
      await uploadFile(roomId, file, currentUser.id, (progressEvent) => {
        const percent = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
        setProgress(percent);
      });
      
      setFile(null);
      setProgress(0);
    } catch (error) {
      console.error('Upload failed:', error);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="file-upload-container">
      <input 
        type="file" 
        onChange={handleFileChange} 
        disabled={isUploading}
      />
      
      {file && (
        <div className="file-info">
          <span>{file.name}</span>
          <button 
            onClick={handleUpload}
            disabled={isUploading}
          >
            {isUploading ? `Uploading... ${progress}%` : 'Upload'}
          </button>
        </div>
      )}
    </div>
  );
};

export default FileUpload;