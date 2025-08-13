import "./globals.css";

export const metadata = {
  title: "NextLevel Food",
  description: "Lets get started!",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
