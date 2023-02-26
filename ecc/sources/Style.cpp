#include "Style.h"

namespace bt {
	constexpr auto ColorFromBytes = [](uint8_t r, uint8_t g, uint8_t b)
{
    return ImVec4((float)r / 255.0f, (float)g / 255.0f, (float)b / 255.0f, 1.0f);
};

	void UseLightTheme()
	{
		ImVec4* colors = ImGui::GetStyle().Colors;
		const ImVec4 bgColor = ColorFromBytes(225, 225, 225);
		const ImVec4 lightBgColor = ColorFromBytes(220, 220, 220);
		const ImVec4 veryLightBgColor = ColorFromBytes(255, 255, 255);

		const ImVec4 panelColor = ColorFromBytes(255, 255, 255);
		const ImVec4 panelHoverColor = ColorFromBytes(175, 215, 255);
		const ImVec4 panelActiveColor = ColorFromBytes(112, 153, 193);

		const ImVec4 textColor = ColorFromBytes(20, 20, 20);
		const ImVec4 textDisabledColor = ColorFromBytes(151, 151, 151);
		const ImVec4 borderColor = ColorFromBytes(78, 78, 78);

		colors[ImGuiCol_Text] = textColor;
		colors[ImGuiCol_TextDisabled] = textDisabledColor;
		colors[ImGuiCol_TextSelectedBg] = panelActiveColor;
		colors[ImGuiCol_WindowBg] = bgColor;
		colors[ImGuiCol_ChildBg] = bgColor;
		colors[ImGuiCol_PopupBg] = bgColor;
		colors[ImGuiCol_Border] = panelActiveColor;
		colors[ImGuiCol_BorderShadow] = borderColor;
		colors[ImGuiCol_FrameBg] = panelColor;
		colors[ImGuiCol_FrameBgHovered] = panelHoverColor;
		colors[ImGuiCol_FrameBgActive] = panelColor;
		colors[ImGuiCol_TitleBg] = bgColor;
		colors[ImGuiCol_TitleBgActive] = bgColor;
		colors[ImGuiCol_TitleBgCollapsed] = bgColor;
		colors[ImGuiCol_MenuBarBg] = bgColor;
		colors[ImGuiCol_ScrollbarBg] = bgColor;
		colors[ImGuiCol_ScrollbarGrab] = ImColor(20, 20, 20, 50);
		colors[ImGuiCol_ScrollbarGrabHovered] = ImColor(20, 20, 20, 100);
		colors[ImGuiCol_ScrollbarGrabActive] = ImColor(20, 20, 20, 30);
		colors[ImGuiCol_CheckMark] = panelActiveColor;
		colors[ImGuiCol_SliderGrab] = panelActiveColor;
		colors[ImGuiCol_SliderGrabActive] = panelHoverColor;
		colors[ImGuiCol_Button] = panelColor;
		colors[ImGuiCol_ButtonHovered] = panelHoverColor;
		colors[ImGuiCol_ButtonActive] = panelHoverColor;
		colors[ImGuiCol_Header] = bgColor;
		colors[ImGuiCol_HeaderHovered] = panelHoverColor;
		colors[ImGuiCol_HeaderActive] = panelActiveColor;
		colors[ImGuiCol_Separator] = borderColor;
		colors[ImGuiCol_SeparatorHovered] = borderColor;
		colors[ImGuiCol_SeparatorActive] = panelHoverColor;
		colors[ImGuiCol_ResizeGrip] = panelColor;
		colors[ImGuiCol_ResizeGripHovered] = panelHoverColor;
		colors[ImGuiCol_ResizeGripActive] = bgColor;
		colors[ImGuiCol_PlotLines] = panelActiveColor;
		colors[ImGuiCol_PlotLinesHovered] = panelHoverColor;
		colors[ImGuiCol_PlotHistogram] = panelActiveColor;
		colors[ImGuiCol_PlotHistogramHovered] = panelHoverColor;
		colors[ImGuiCol_DragDropTarget] = bgColor;
		colors[ImGuiCol_NavHighlight] = bgColor;
		colors[ImGuiCol_DockingPreview] = panelActiveColor;
		colors[ImGuiCol_Tab] = bgColor;
		colors[ImGuiCol_TabActive] = panelActiveColor;
		colors[ImGuiCol_TabUnfocused] = bgColor;
		colors[ImGuiCol_TabUnfocusedActive] = panelActiveColor;
		colors[ImGuiCol_TabHovered] = panelHoverColor;

		// Docking
		colors[ImGuiCol_DockingPreview] = ColorFromBytes(0, 85, 70);

		auto& style = ImGui::GetStyle();
		style.TabRounding = 8.0f;
		style.ScrollbarRounding = 5.0f;
		style.WindowRounding = 8.0f;
		style.GrabRounding = 8.0f;
		style.FrameRounding = 8.0f;
		style.PopupRounding = 8.0f;
		style.ChildRounding = 8.0f;
		style.WindowMinSize = {220, 100};
		style.WindowTitleAlign = {0.5f, 0.5f};
		style.WindowBorderSize = 0.0f;
	}
}