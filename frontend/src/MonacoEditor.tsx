import Editor from "@monaco-editor/react";

type MonacoEditorProps = {
  value: string;
  language: string;
  theme: string;
  height: number;
  onChange: (value: string) => void;
};

export default function MonacoEditor({
  value,
  language,
  theme,
  height,
  onChange,
}: MonacoEditorProps) {
  return (
    <Editor
      height={`${height}px`}
      language={language}
      theme={theme}
      value={value}
      options={{
        minimap: {
          enabled: false,
        },
        fontSize: 14,
        automaticLayout: true,
        scrollBeyondLastLine: false,
      }}
      onChange={(value) => onChange(value ?? "")}
    />
  );
}