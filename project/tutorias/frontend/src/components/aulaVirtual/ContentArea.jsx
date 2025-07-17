// components/VirtualClassroom/ContentArea.jsx
import React from 'react';
import PropTypes from 'prop-types';
import Whiteboard from '../Whiteboard/Whiteboard';
import DocumentSharing from './Documents/DocumentSharing';

const ContentArea = ({ activeTab, documents, onUpload, whiteboardRef, sessionId }) => {
  if (activeTab === 'whiteboard') {
    return <Whiteboard ref={whiteboardRef} sessionId={sessionId} />;
  }

  if (activeTab === 'documents') {
    return <DocumentSharing documents={documents} onUpload={onUpload} />;
  }

  return null;
};

ContentArea.propTypes = {
  activeTab: PropTypes.oneOf(['whiteboard', 'documents']).isRequired,
  documents: PropTypes.array,
  onUpload: PropTypes.func,
  whiteboardRef: PropTypes.oneOfType([
    PropTypes.func, 
    PropTypes.shape({ current: PropTypes.any })
  ]),
  sessionId: PropTypes.string.isRequired,
};

ContentArea.defaultProps = {
  documents: [],
  onUpload: () => {},
  whiteboardRef: null,
};

export default ContentArea;

