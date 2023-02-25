#include "MainWindow.h"

namespace bt 
{
    void delay()
    {
        auto start = std::chrono::high_resolution_clock::now();
        auto stop = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        while (true)
        {
            stop = std::chrono::high_resolution_clock::now();
            duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
            if (duration.count() >= 9000)
            {
                return;
            }
            else
                std::this_thread::sleep_for(std::chrono::milliseconds(9));
        }
    }

    MainWindow::MainWindow()
    {
        this->window = nullptr;
        this->io = nullptr;
        this->running = false;
        this->success = false;

        if (glfwInit())
        {
            const char* glsl_version = "#version 330";
            glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
            glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
            glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
            //glfwWindowHint(GLFW_TRANSPARENT_FRAMEBUFFER, GLFW_TRUE);
            glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
           



            this->window = glfwCreateWindow(1, 1, "Електронно-графічна Формула", NULL, NULL);
            if (this->window)
            {
                glfwHideWindow(window);
                init(this);
                glfwSetKeyCallback(window, OnKeyCallback);
                glfwSetScrollCallback(window, OnScrollCallback);
                glfwSetWindowSizeCallback(window, OnWindowResizeCallback);
                glfwSetWindowCloseCallback(window, OnWindowCloseCallback);
                //glfwSetWindowAttrib(window, GLFW_DECORATED, GLFW_FALSE);

                glfwMakeContextCurrent(this->window);
                glfwSwapInterval(1); // Enable vsync

                // Setup Dear ImGui context
                IMGUI_CHECKVERSION();
                ImGui::CreateContext();
                this->io = &(ImGui::GetIO()); (void)io;
                this->io->Fonts->AddFontFromFileTTF("C:\\Windows\\Fonts\\calibri.ttf", 16.0f, NULL, io->Fonts->GetGlyphRangesCyrillic());
                this->io->IniFilename = nullptr;
                
                io->ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;
                io->ConfigFlags |= ImGuiConfigFlags_ViewportsEnable;
                io->ConfigFlags |= ImGuiConfigFlags_IsSRGB;
                io->ConfigViewportsNoAutoMerge = true;

                UseLightTheme();

                
                ImGui_ImplGlfw_InitForOpenGL(this->window, true);
                ImGui_ImplOpenGL3_Init(glsl_version);

                this->clear_color = ImVec4(0.0f, 0.0f, 0.0f, 1.0f);
                this->success = true;
            }
            else
            {
                this->success = false;
            }
        }
        else
        {
            this->success = false;
        }
    }

    void MainWindow::Loop()
    {
        if (this->success)
        {
            this->running = true;
            bool sff = true;
            int counter = 0;
            float some_float = 0.4;
            
            while (!glfwWindowShouldClose(this->window) && this->running)
            {
                glfwPollEvents();
                Render();
            }
        }
    }
   
    void MainWindow::Render() 
    {
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();

        RenderGUI();
        ImGui::Render();

        int display_w, display_h;
        glfwGetFramebufferSize(this->window, &display_w, &display_h);
        glViewport(0, 0, display_w, display_h);
        glClearColor(clear_color.x * clear_color.w, clear_color.y * clear_color.w, clear_color.z * clear_color.w, clear_color.w);
        glClear(GL_COLOR_BUFFER_BIT);
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        if (this->io->ConfigFlags & ImGuiConfigFlags_ViewportsEnable)
        {
            GLFWwindow* backup_current_context = glfwGetCurrentContext();
            ImGui::UpdatePlatformWindows();
            ImGui::RenderPlatformWindowsDefault();
            glfwMakeContextCurrent(backup_current_context);
        }

        glfwSwapBuffers(this->window);
        delay();
    }

    void MainWindow::RenderGUI()
    {
        ImGuiWindowFlags win_flags = 0;
        win_flags |= ImGuiWindowFlags_HorizontalScrollbar | ImGuiWindowFlags_NoCollapse;

        static bool first_time = true;
        if (first_time)
        {
            ImGui::SetNextWindowSize({ 600, 400 });
            first_time = false;
        }

        ImGui::Begin(u8"Електронно-графічна Формула", &running, win_flags);

        ImGui::End();
    }

    MainWindow::~MainWindow()
    {
        ImGui_ImplOpenGL3_Shutdown();
        ImGui_ImplGlfw_Shutdown();
        ImGui::DestroyContext();

        glfwDestroyWindow(this->window);
        glfwTerminate();
    }

    void MainWindow::init(Window* window)
    {
        window->setNativeWindow(this->window);
        glfwSetWindowUserPointer(this->window, window);
    }

    void MainWindow::OnScroll(float delta)
    {
        
    }

    void MainWindow::OnKey(int key, int scan_code, int action, int mods)
    {

    }

    void MainWindow::OnResize(int width, int height)
    {
        this->size.x = width;
        this->size.y = height;
        this->Render();
    }

    void MainWindow::OnClose()
    {
        running = false;
    }

    static void OnKeyCallback(GLFWwindow* window, int key, int scan_code, int action, int mods)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnKey(key, scan_code, action, mods);
    }

    static void OnScrollCallback(GLFWwindow* window, double x_offset, double y_offset)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnScroll(y_offset);
    }

    static void OnWindowResizeCallback(GLFWwindow* window, int width, int height)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnResize(width, height);
    }

    static void OnWindowCloseCallback(GLFWwindow* window)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnClose();
    }
}