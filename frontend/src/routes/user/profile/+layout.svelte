<script>
	import { currActiveProfPage } from './store.js';

	const handleClick = (e, source) => {
		currActiveProfPage.set(source);
	};
</script>

<div class="bg-gradient-to-r from-slate-700 to-slate-900 flex justify-center w-[100vw] h-[100vh]">
	<div class="bg-white h-full w-[80%] rounded-2xl flex justify-between pr-16 overflow-hidden">
		<div class="bg-gray-500 h-full w-[20%] flex flex-col items-center justify-center">
			<nav
				class="list-none bg-gray-400 font-semibold font-mono text-white w-full py-5 flex flex-col justify-center h-[40%]"
			>
				<button
					on:click={(e) => handleClick(e, 'Profile')}
					class={'py-1.5 px-5 text-left' +
						($currActiveProfPage === 'Profile' ? ' bg-gray-700' : '')}
				>
					Profile
				</button>
				<button
					on:click={(e) => handleClick(e, 'Photo')}
					class={'py-1.5 px-5 text-left' + ($currActiveProfPage === 'Photo' ? ' bg-gray-700' : '')}
				>
					Photo
				</button>
				<button
					on:click={(e) => handleClick(e, 'Account Security')}
					class={'py-1.5 px-5 text-left' + ($currActiveProfPage === 'Account Security' ? ' bg-gray-700' : '')}
				>
					Account Security
				</button>
				<button
					on:click={(e) => handleClick(e, 'Close Account')}
					class={'py-1.5 px-5 text-left' + ($currActiveProfPage === 'Close Account' ? ' bg-gray-700' : '')}
				>
					Close Account
				</button>
				<button class="text-red-600 p-5 text-left">Logout</button>
			</nav>
		</div>
		<slot />
	</div>
</div>
