//このプログラムは二つの予定表を同期するプログラムだ。 
//エラーが起こっている修正せよ 
 
using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Net.Http; 
using System.Net.Http.Headers; 
using System.Threading.Tasks; 
using Newtonsoft.Json; 
 
namespace OutlookCalendarSync 
{ 
    class Program 
    { 
        static HttpClient client = new HttpClient(); 
 
        static void Main(string[] args) 
        { 
            // Get the access tokens for both accounts 
            string so12ra16AccessToken = GetAccessToken("so12ra16@outlook.jp", "Microsoft365"); 
            string dendaiAccessToken = GetAccessToken("20ec070@ms.dendai.ac.jp", "Microsoft365"); 
 
            // Get the calendar events for both accounts 
            List<CalendarEvent> so12ra16Events = GetCalendarEvents(so12ra16AccessToken).Result; 
            List<CalendarEvent> dendaiEvents = GetCalendarEvents(dendaiAccessToken).Result; 
 
            // Merge the events and remove duplicates 
            List<CalendarEvent> mergedEvents = so12ra16Events.Union(dendaiEvents, new CalendarEventComparer()).ToList(); 
 
            // Save the merged events to both accounts 
            foreach (var e in mergedEvents) 
            { 
                SaveCalendarEvent(so12ra16AccessToken, e).Wait(); 
                SaveCalendarEvent(dendaiAccessToken, e).Wait(); 
            } 
 
            Console.WriteLine("Calendar events synced successfully."); 
            Console.ReadKey(); 
        } 
 
        static async Task<List<CalendarEvent>> GetCalendarEvents(string accessToken) 
        { 
            List<CalendarEvent> events = new List<CalendarEvent>(); 
 
            // Set up the API request 
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken); 
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json")); 
            string url = "https://outlook.office.com/api/v2.0/me/events"; 
            string query = "?$select=Subject,Start,End&$top=1000"; 
            string response = ""; 
 
            // Fetch the events 
            do 
            { 
                HttpResponseMessage message = await client.GetAsync(url + query); 
                if (message.IsSuccessStatusCode) 
                { 
                    response = await message.Content.ReadAsStringAsync(); 
                    events.AddRange(JsonConvert.DeserializeObject<List<CalendarEvent>>(response)); 
                    query = JsonConvert.DeserializeObject<ODataNextLink>(response).odata_nextLink; 
                } 
                else 
                { 
                    response = await message.Content.ReadAsStringAsync(); 
                    throw new Exception("Error fetching calendar events: " + response); 
                } 
            } while (!string.IsNullOrEmpty(query)); 
 
            return events; 
        } 
 
        static async Task SaveCalendarEvent(string accessToken, CalendarEvent e) 
        { 
            // Set up the API request 
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken); 
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json")); 
            string url = "https://outlook.office.com/api/v2.0/me/events/" + e.Id; 
 
            // Update the event 
            var content = new StringContent(JsonConvert.SerializeObject(e), System.Text.Encoding.UTF8, "application/json"); 
            HttpResponseMessage message = await client.PatchAsync(url, content); 
 
            if (!message.IsSuccessStatusCode) 
            { 
                string response = await message.Content.ReadAsStringAsync(); 
                throw new Exception("Error saving calendar event: " + response); 
            } 
        } 
 
        static string GetAccessToken(string email, string password) 
        { 
            // Authenticate with Outlook using OAuth2 
            // and get an access token 
            // You will need to create a new Azure AD application, 
            // grant it access to the Outlook API, and configure 
            // the redirect URI before this will work 
 
            // Using a dummy access token for now 
            return "dummy-access-token"; 
        } 
    } 
 
    // C# class for deserializing Outlook calendar events 
    class CalendarEvent 
    { 
        public string Id { get; set; } 
        public string Subject { get; set; } 
        public DateTime Start { get; set; } 
        public DateTime End { get; set; } 
 
        public override bool Equals(object obj) 
        { 
            if (obj == null || GetType() != obj.GetType()) 
            { 
                return false; 
            } 
 
            CalendarEvent other = (CalendarEvent)obj; 
            return Id == other.Id; 
        } 
 
        public override int GetHashCode() 
        { 
            return Id.GetHashCode(); 
        } 
    } 
 
    class CalendarEventComparer : IEqualityComparer<CalendarEvent> 
    { 
        public bool Equals(CalendarEvent x, CalendarEvent y) 
        { 
            return x.Id == y.Id; 
        } 
 
        public int GetHashCode(CalendarEvent obj) 
        { 
            return obj.Id.GetHashCode(); 
        } 
    } 
 
    // C# class for deserializing Outlook next link URLs 
    class ODataNextLink 
    { 
        public string odata_nextLink { get; set; } 
    } 
}  