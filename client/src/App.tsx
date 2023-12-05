import React from "react";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import FeedView from "./pages/Feed/FeedView";
import LibraryView from "./pages/Library/LibraryView";
import SettingsView from "./pages/Settings/SettingsView";
import MessengerView from "./pages/Messenger/MessengerView";
import ProfileView from "./pages/Profile/ProfileView";
import CreatePostView from "./pages/CreatePost/CreatePostView";
import SidebarView from "./components/SidebarView";
import "react-loading-skeleton/dist/skeleton.css";

const App: React.FC = () => {
  const hideSidebarOnCreatePost = window.location.pathname === "/create-post";

  return (
    <div className="App">
      <BrowserRouter>
        <div className="flex">
          {!hideSidebarOnCreatePost && <SidebarView />}
          <Routes>
            <Route path="/" element={<FeedView />} />
            <Route path="/feed" element={<FeedView />} />
            <Route path="/library" element={<LibraryView />} />
            <Route path="/settings" element={<SettingsView />} />
            <Route path="/messenger" element={<MessengerView />} />
            <Route path="/profile" element={<ProfileView />} />
            <Route path="/create-post" element={<CreatePostView />} />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
};

export default App;
