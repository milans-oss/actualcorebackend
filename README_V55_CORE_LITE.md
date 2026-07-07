# DFP2 Backend v55 Core Lite

Deploy this as the main/core backend with persistent disk. It serves Lead Pool, PM shortlisting, ranking, contact tracker, admin undo/redo, edit locks and transfer. It blocks repository/search/story endpoints so heavy jobs cannot crash the core workflow service.

Set `DFP2_SERVICE_ROLE=core`.
